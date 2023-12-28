from rest_framework.decorators import api_view, permission_classes, parser_classes
from rest_framework.response import Response
from rest_framework import status
from users.permissions import UserActive
from rest_framework.parsers import FormParser, MultiPartParser
from memberships.models import AdMembership, UserMembership
from varieties.models import SubCategory, Currency, Country, City, Size, PaymentMethod, RentPeriod
from Ad.models import AdPicture
from apartments.models import NearLocation, Interface, AdjustedTo, RoomCounts, BathroomCounts, FloorsCounts, BuildingAge, Amenity, AdditionalFeature, EstateType, RealEstate
from globals.payment_helpers import create_charge, create_customer
from globals.global_tasks import reward_user
from globals.ad_helpers import update_ad_type
from django.conf import settings


def create_ad(user, sub_category, title, description, country_model, city_model, currency_model, payment_method_model, price, full_name=None, phone_number=None, lat=None, lat_delta=None, long=None, long_delta=None, is_delivery=False, condition_model=None, size_model=None, rent_period_model=None, near_location_model=None, interface_model=None, adjusted_to_model=None, room_counts_model=None, bathroom_counts_model=None, floor_counts_model=None, building_age_model=None, estate_country_model=None, estate_type_model=None, is_rental=None):
    ad = RealEstate.objects.create(
        user=user,
        category=sub_category,
        ad_title=title,
        ad_description=description,
        country=country_model,
        city=city_model,
        currency=currency_model,
        payment_method=payment_method_model,
        price=price,
        full_name=full_name,
        phone_number=phone_number,
        lat=lat,
        lat_delta=lat_delta,
        long=long,
        long_delta=long_delta,
        is_delivery=is_delivery,
        condition=condition_model,
        size=size_model,
        rent_period=rent_period_model,
        near_location=near_location_model,
        interface=interface_model,
        adjusted_to=adjusted_to_model,
        room_counts=room_counts_model,
        bathroom_count=bathroom_counts_model,
        floor_count=floor_counts_model,
        building_age=building_age_model,
        estate_country=estate_country_model,
        estate_type=estate_type_model,
        is_rental=is_rental
    )
    return ad


def add_amenities(ad, features):
    for feature in features:
        try:
            amenity = Amenity.objects.get(name=feature)
        except Amenity.DoesNotExist:
            return Response({
                "message": f"Amenity with name {feature} doesn't exist"
            }, status=status.HTTP_404_NOT_FOUND)
        ad.amenities.append(amenity)


def add_additional_features(ad, features):
    for feature in features:
        try:
            additional_feature = AdditionalFeature.objects.get(name=feature)
        except AdditionalFeature.DoesNotExist:
            return Response({
                "message": f"Additional feature with name {feature} doesn't exist"
            }, status=status.HTTP_404_NOT_FOUND)
        ad.additional_features.append(additional_feature)


def add_images(ad, ad_images):
    for image in ad_images:
        AdPicture.objects.create(
            ad=ad,
            image=image
        )


@api_view(["POST"])
@permission_classes([UserActive])
@parser_classes([FormParser, MultiPartParser])
def publish_ad(request):
    data = request.data
    user = request.user

    if not data or data == None:
        return Response({
            "message": "Please Provide the needed data to publish your ad!"
        }, status=status.HTTP_400_BAD_REQUEST)

    # * These data are mandatory, and mostly doesn't change over the time
    category = data.get("category")
    title = data.get("title")
    description = data.get("description")
    price = data.get("price")
    currency = data.get("currency")
    country = data.get("country")
    city = data.get("city")
    ad_images = request.FILES.getlist("ad_images")
    payment_method = data.get("payment_method")
    lat = data.get("lat")
    lat_delta = data.get("lat_delta")
    long_delta = data.get("long_delta")
    long = data.get("long")
    membership_name = data.get("membership_name")
    full_name = data.get("full_name")
    phone_number = data.get("phone_number")
    is_delivery = bool(data.get("is_delivery"))
    size = data.get('size')
    rent_period = data.get('rent_period')
    near_location = data.get('near_location')
    interface = data.get('interface')
    adjusted_to = data.get('adjusted_to')
    room_counts = data.get('room_count')
    bathroom_counts = data.get('bathroom_counts')
    floor_count = data.get('floor_count')
    building_age = data.get('building_age')
    estate_country = data.get('estate_country')
    estate_type = data.get('estate_type')
    amenities = data.get('amenities')
    additional_features = data.get("additional_features")
    is_rental = bool(data.get("is_rental"))
    size_model = None
    near_location_model = None
    # interface_model = None
    adjusted_to_model = None
    estate_country_model = None
    estate_type_model = None

    if not category or category == "":
        return Response({
            "message": "Please enter category"
        }, status=status.HTTP_400_BAD_REQUEST)

    try:
        sub_category = SubCategory.objects.get(name=category)
    except SubCategory.DoesNotExist:
        return Response({
            "message": "This category doesn't exists"
        }, status=status.HTTP_404_NOT_FOUND)

    if not title:
        return Response({
            "message": "Please enter title"
        }, status=status.HTTP_400_BAD_REQUEST)

    if not description:
        return Response({
            "message": "Please enter description"
        }, status=status.HTTP_400_BAD_REQUEST)

    if not price:
        return Response({
            "message": "Please enter price"
        }, status=status.HTTP_400_BAD_REQUEST)

    if not currency:
        return Response({
            "message": "Please enter currency"
        }, status=status.HTTP_400_BAD_REQUEST)

    try:
        currency_model = Currency.objects.get(name=currency)
    except Currency.DoesNotExist:
        return Response({
            "message": "this currency doesn't exists"
        }, status=status.HTTP_404_NOT_FOUND)

    if not country:
        return Response({
            "message": "Please enter country"
        }, status=status.HTTP_400_BAD_REQUEST)

    try:
        country_model = Country.objects.get(name=country)
    except Country.DoesNotExist:
        return Response({
            "message": "There's no country with this name"
        }, status=status.HTTP_404_NOT_FOUND)

    if not city:
        return Response({
            "message": "Please enter city"
        }, status=status.HTTP_400_BAD_REQUEST)

    try:
        city_model = City.objects.get(name=city)
    except City.DoesNotExist:
        return Response({
            "message": "There's no city with this name"
        }, status=status.HTTP_404_NOT_FOUND)

    if not payment_method:
        return Response({
            "message": "Please enter city"
        }, status=status.HTTP_400_BAD_REQUEST)

    try:
        payment_method_model = PaymentMethod.objects.get(name=payment_method)
    except PaymentMethod.DoesNotExist:
        return Response({
            "message": "There's no payment method with this name"
        }, status=status.HTTP_404_NOT_FOUND)

    if not ad_images or len(ad_images) == 0:
        return Response({
            "message": "please provide images for your ad"
        }, status=status.HTTP_400_BAD_REQUEST)

    if size:
        try:
            size_model = Size.objects.get(name=size)
        except Size.DoesNotExist:
            return Response({
                "message": "There's no size with this name"
            }, status=status.HTTP_404_NOT_FOUND)

    if near_location:
        try:
            near_location_model = NearLocation.objects.get(name=near_location)
        except NearLocation.DoesNotExist:
            return Response({
                "message": "There's no near location with this name"
            }, status=status.HTTP_404_NOT_FOUND)

    if adjusted_to:
        try:
            adjusted_to_model = AdjustedTo.objects.get(name=adjusted_to)
        except AdjustedTo.DoesNotExist:
            return Response({
                "message": "There's no adjusted_to with this name"
            }, status=status.HTTP_404_NOT_FOUND)

    if estate_country:
        try:
            estate_country_model = Country.objects.get(
                name=estate_country)
        except Country.DoesNotExist:
            return Response({
                "message": "There's no estate country with this name"
            }, status=status.HTTP_404_NOT_FOUND)

    if estate_type:
        try:
            estate_type_model = EstateType.objects.get(name=estate_type)
        except EstateType.DoesNotExist:
            return Response({
                "message": "There's no estate type with this name"
            }, status=status.HTTP_404_NOT_FOUND)

    user_membership = None
    try:
        user_membership = UserMembership.objects.get(subscriber=user)
    except UserMembership.DoesNotExist:
        pass

    # * if the user has a membership, we'll feature his Ad
    if user_membership != None:
        base_user_membership = user_membership.membership
        try:
            ad = create_ad(
                user=user,
                sub_category=sub_category,
                currency_model=currency_model,
                title=title,
                description=description,
                country_model=country_model,
                city_model=city_model,
                payment_method_model=payment_method_model,
                price=price,
                full_name=full_name,
                phone_number=phone_number,
                lat=lat,
                lat_delta=lat_delta,
                long=long,
                long_delta=long_delta,
                is_delivery=is_delivery,
                size_model=size_model,
                rent_period_model=rent_period,
                near_location_model=near_location_model,
                interface_model=interface,
                adjusted_to_model=adjusted_to_model,
                room_counts_model=room_counts,
                bathroom_counts_model=bathroom_counts,
                floor_counts_model=floor_count,
                building_age_model=building_age,
                estate_country_model=estate_country_model,
                estate_type_model=estate_type_model,
                is_rental=is_rental
            )
            add_amenities(ad, amenities)
            add_additional_features(ad, additional_features)
            add_images(ad, ad_images)
            update_ad_type(base_user_membership, ad)
            reward_user(user, ad)
            return Response({
                "message": "Congratulations! your ad is available now!"
            }, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response({
                "message": "an error occurred while publishing your ad, please try again"
            }, status=status.HTTP_400_BAD_REQUEST)

    elif membership_name:
        stripe_token = data.get("stripe_token")
        try:
            membership = AdMembership.objects.get(name=membership_name)
        except AdMembership.DoesNotExist:
            return Response({
                "message": "There's no membership with this name!"
            }, status=status.HTTP_404_NOT_FOUND)

        try:
            customer = create_customer(user, stripe_token)
        except Exception as e:
            return Response({
                "message": "there's an error occurred while processing the payment, please try again"
            }, status=status.HTTP_400_BAD_REQUEST)

        try:
            create_charge(customer, membership.price,
                          description="Featuring Ad")
        except Exception as e:
            return Response({
                "message": "there's an error occurred while processing the payment, please try again"
            }, status=status.HTTP_400_BAD_REQUEST)

        try:
            ad = create_ad(
                user=user,
                sub_category=sub_category,
                currency_model=currency_model,
                title=title,
                description=description,
                country_model=country_model,
                city_model=city_model,
                payment_method_model=payment_method_model,
                price=price,
                full_name=full_name,
                phone_number=phone_number,
                lat=lat,
                lat_delta=lat_delta,
                long=long,
                long_delta=long_delta,
                is_delivery=is_delivery,
                size_model=size_model,
                rent_period_model=rent_period,
                near_location_model=near_location_model,
                interface_model=interface,
                adjusted_to_model=adjusted_to_model,
                room_counts_model=room_counts,
                bathroom_counts_model=bathroom_counts,
                floor_counts_model=floor_count,
                building_age_model=building_age,
                estate_country_model=estate_country_model,
                estate_type_model=estate_type_model,
                is_rental=is_rental
            )
            add_amenities(ad, amenities)
            add_additional_features(ad, additional_features)
            add_images(ad, ad_images)
            update_ad_type(membership, ad)
            reward_user(user, ad)
            return Response({
                "message": "Congratulations! your ad is available now!"
            }, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response({
                "message": "an error occurred while publishing your ad, please try again"
            }, status=status.HTTP_400_BAD_REQUEST)

    else:
        try:
            ad = create_ad(
                user=user,
                sub_category=sub_category,
                currency_model=currency_model,
                title=title,
                description=description,
                country_model=country_model,
                city_model=city_model,
                payment_method_model=payment_method_model,
                price=price,
                full_name=full_name,
                phone_number=phone_number,
                lat=lat,
                lat_delta=lat_delta,
                long=long,
                long_delta=long_delta,
                is_delivery=is_delivery,
                size_model=size_model,
                rent_period_model=rent_period,
                near_location_model=near_location_model,
                interface_model=interface,
                adjusted_to_model=adjusted_to_model,
                room_counts_model=room_counts,
                bathroom_counts_model=bathroom_counts,
                floor_counts_model=floor_count,
                building_age_model=building_age,
                estate_country_model=estate_country_model,
                estate_type_model=estate_type_model,
                is_rental=is_rental
            )
            add_amenities(ad, amenities)
            add_additional_features(ad, additional_features)
            add_images(ad, ad_images)
            return Response({
                "message": "Congratulations! your ad is available now!"
            }, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response({
                "message": "an error occurred while publishing your ad, please try again"
            }, status=status.HTTP_400_BAD_REQUEST)
