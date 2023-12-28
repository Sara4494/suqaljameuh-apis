from rest_framework.decorators import api_view, permission_classes, parser_classes
from rest_framework.response import Response
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework import status
from django.core import exceptions
from users.permissions import UserActive
from varieties.models import SubCategory, Currency, Country, City, Size, PaymentMethod, RentPeriod
from Ad.models import AdPicture
from apartments.models import NearLocation, Interface, AdjustedTo, RoomCounts, BathroomCounts, FloorsCounts, BuildingAge, Amenity, AdditionalFeature, EstateType
from apartments.models import RealEstate
from users.permissions import UserOwnerOnly


def add_images(ad, ad_images):
    for image in ad_images:
        AdPicture.objects.create(
            ad=ad,
            image=image
        )


def delete_images(ad, past_ad_images):
    for past_pic in past_ad_images:
        past_pic.delete()


def add_amenities(ad, amenities):
    amenities_list = []
    for amenity in amenities:
        try:
            amenity_model = Amenity.objects.get(name=amenity)
            amenities_list.append(amenity_model)
        except Amenity.DoesNotExist:
            return Response({
                "message": f"couldn't find amenity with name {amenity}"
            }, status=status.HTTP_404_NOT_FOUND)
    ad.amenities.set(amenities_list)


def add_additional_features(ad, additional_features):
    additional_features_list = []
    for feature in additional_features:
        try:
            additional_feature = AdditionalFeature.objects.get(name=feature)
            additional_features_list.append(additional_feature)
        except AdditionalFeature.DoesNotExist:
            return Response({
                "message": f"couldn't find feature with name {feature}"
            }, status=status.HTTP_404_NOT_FOUND)
    ad.additional_features.set(additional_features_list)


@api_view(["POST"])
@permission_classes([UserActive, UserOwnerOnly])
@parser_classes([FormParser, MultiPartParser])
def update_ad(request, ad_id):
    data = request.data

    if not data or data == None:
        return Response({
            "message": "Please Provide the needed data to update your ad!"
        }, status=status.HTTP_400_BAD_REQUEST)

    # * These data are mandatory, and mostly doesn't change over the time
    category = data.get("category")
    title = data.get("title")
    description = data.get("description")
    price = data.get("price")
    currency = data.get("currency")
    country = data.get("country")
    city = data.get("city")
    ad_images = data.get("ad_images")
    payment_method = data.get("payment_method")
    lat = data.get("lat")
    lat_delta = data.get("lat_delta")
    long_delta = data.get("long_delta")
    long = data.get("long")
    full_name = data.get("full_name")
    phone_number = data.get("phone_number")
    is_delivery = data.get("is_delivery")
    size = data.get('size')
    rent_period = data.get('rent_period')
    near_location = data.get('near_location')
    interface = data.get('interface')
    adjusted_to = data.get('adjusted_to')
    room_counts = data.get('room_counts')
    bathroom_counts = data.get('bathroom_counts')
    floor_count = data.get('floor_count')
    building_age = data.get('building_age')
    estate_country = data.get('estate_country')
    estate_type = data.get('estate_type')
    amenities = data.get('')
    additional_features = data.get("")
    size_model = None

    try:
        ad = RealEstate.objects.get(pk=ad_id)
    except exceptions.ObjectDoesNotExist:
        return Response({
            "message": "This Ad Doesn't Exists Or Maybe The Publisher Deleted It"
        }, status=status.HTTP_404_NOT_FOUND)

    try:
        is_updated = False
        if category and ad.category.name != category:
            try:
                sub_category = SubCategory.objects.get(name=category)
            except SubCategory.DoesNotExist:
                return Response({
                    "message": "This category doesn't exists"
                }, status=status.HTTP_404_NOT_FOUND)
            ad.category = sub_category
            is_updated = True
        if title and ad.ad_title != title:
            ad.ad_title = title
            is_updated = True

        if description and ad.ad_description != description:
            ad.ad_description = description
            is_updated = True

        if price and ad.price != price:
            ad.price = price
            is_updated = True

        if full_name and ad.full_name != full_name:
            ad.full_name = full_name
            is_updated = True

        if phone_number and ad.phone_number != phone_number:
            ad.phone_number = phone_number
            is_updated = True

        if is_delivery and ad.is_delivery != is_delivery:
            ad.is_delivery = is_delivery
            is_updated = True

        if price and ad.price != price:
            ad.price = price
            is_updated = True

        if lat and ad.lat != lat:
            ad.lat = lat
            is_updated = True

        if lat_delta and ad.lat_delta != lat_delta:
            ad.lat_delta = lat_delta
            is_updated = True

        if long and ad.long != long:
            ad.long = long
            is_updated = True

        if long_delta and ad.long_delta != long_delta:
            ad.long_delta = long_delta
            is_updated = True

        if currency and ad.currency.name != currency:
            try:
                currency_model = Currency.objects.get(name=currency)
            except Currency.DoesNotExist:
                return Response({
                    "message": "this currency doesn't exists"
                }, status=status.HTTP_404_NOT_FOUND)
            ad.currency = currency_model
            is_updated = True

        if country and ad.country.name != country:
            try:
                country_model = Country.objects.get(name=country)
            except Country.DoesNotExist:
                return Response({
                    "message": "this country doesn't exists"
                }, status=status.HTTP_404_NOT_FOUND)
            ad.country = country_model
            is_updated = True

        if city and ad.city.name != city:
            try:
                city_model = City.objects.get(name=city)
            except City.DoesNotExist:
                return Response({
                    "message": "this city doesn't exists"
                }, status=status.HTTP_404_NOT_FOUND)
            ad.city = city_model
            is_updated = True

        if payment_method and ad.payment_method.name != payment_method:
            try:
                payment_method_model = PaymentMethod.objects.get(
                    name=payment_method)
            except PaymentMethod.DoesNotExist:
                return Response({
                    "message": "this payment method doesn't exists"
                }, status=status.HTTP_404_NOT_FOUND)
            ad.payment_method = payment_method_model
            is_updated = True

        if size and ad.size.name != size:
            try:
                size_model = Size.objects.get(name=size)
            except Size.DoesNotExist:
                return Response({
                    "message": "this size doesn't exists"
                }, status=status.HTTP_404_NOT_FOUND)
            ad.size = size_model
            is_updated = True

        if rent_period and ad.rent_period != rent_period:
            ad.rent_period = rent_period
            is_updated = True

        if near_location and ad.near_location.name != near_location:
            try:
                near_location_model = NearLocation.objects.get(
                    name=near_location)
            except NearLocation.DoesNotExist:
                return Response({
                    "message": "this near location doesn't exists"
                }, status=status.HTTP_404_NOT_FOUND)
            ad.near_location = near_location_model
            is_updated = True

        if interface and ad.interface.name != interface:
            try:
                interface_model = Interface.objects.get(name=interface)
            except Interface.DoesNotExist:
                return Response({
                    "message": "this interface doesn't exists"
                }, status=status.HTTP_404_NOT_FOUND)
            ad.interface = interface_model
            is_updated = True

        if adjusted_to and ad.adjusted_to.name != adjusted_to:
            try:
                adjusted_to_model = AdjustedTo.objects.get(name=adjusted_to)
            except AdjustedTo.DoesNotExist:
                return Response({
                    "message": "this adjusted to doesn't exists"
                }, status=status.HTTP_404_NOT_FOUND)
            ad.adjusted_to = adjusted_to_model
            is_updated = True

        if room_counts and ad.room_counts != room_counts:
            ad.room_counts = room_counts
            is_updated = True

        if bathroom_counts and ad.bathroom_counts != bathroom_counts:
            ad.bathroom_counts = bathroom_counts
            is_updated = True

        if floor_count and ad.floor_count != floor_count:
            ad.floor_count = floor_count
            is_updated = True

        if building_age and ad.building_age != building_age:
            ad.building_age = building_age
            is_updated = True

        if interface and ad.interface != interface:
            ad.interface = interface
            is_updated = True

        if estate_country and ad.estate_country.name != estate_country:
            try:
                estate_country_model = Country.objects.get(
                    name=estate_country)
            except Country.DoesNotExist:
                return Response({
                    "message": "this estate country doesn't exists"
                }, status=status.HTTP_404_NOT_FOUND)
            ad.estate_country = estate_country_model
            is_updated = True

        if estate_type and ad.estate_type.name != estate_type:
            try:
                estate_type_model = EstateType.objects.get(name=estate_type)
            except EstateType.DoesNotExist:
                return Response({
                    "message": "this estate type doesn't exists"
                }, status=status.HTTP_404_NOT_FOUND)
            ad.estate_type = estate_type_model
            is_updated = True

        if amenities:
            add_amenities(ad, amenities)

        if additional_features:
            add_amenities(ad, additional_features)

        if ad_images:
            try:
                past_ad_images = AdPicture.objects.filter(ad=ad)
                delete_images(ad, past_ad_images)
            except Exception as e:
                return Response({
                    "message": "an error occurred while updating the photos"
                }, status=status.HTTP_400_BAD_REQUEST)
            try:
                add_images(ad, ad_images)
            except Exception as e:
                return Response({
                    "message": "an error occurred while updating the photos"
                }, status=status.HTTP_400_BAD_REQUEST)
            is_updated = True
        if is_updated == True:
            ad.save()
            return Response({
                "message": "The ad was updated successfully!"
            }, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        print(e)
        return Response({
            "message": "an error occurred while updating the ad, please try again."
        }, status=status.HTTP_400_BAD_REQUEST)
