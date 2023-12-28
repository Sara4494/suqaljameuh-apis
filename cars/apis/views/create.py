from rest_framework.decorators import api_view, permission_classes, parser_classes
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.response import Response
from rest_framework import status
from users.permissions import UserActive
from memberships.models import AdMembership, UserMembership
from varieties.models import SubCategory, Currency, Country, City, Brand, SubType, Type, Size, Colors, Condition, PaymentMethod, Model, KiloMeter
from Ad.models import AdPicture
from cars.models import Car, TransmissionType, RentPeriod, FoulType, InternalSpecs, OuterSpecs, RegionalSpecs
from globals.payment_helpers import create_charge, create_customer
from globals.global_tasks import reward_user
from globals.ad_helpers import update_ad_type
from django.conf import settings

import stripe
stripe.api_key = settings.STRIPE_PRIVATE_KEY


def create_ad(user, sub_category, title, description, country_model, city_model, currency_model, payment_method_model, price, full_name=None, phone_number=None, lat=None, lat_delta=None, long=None, long_delta=None, is_delivery=False, brand_model=None, color_model=None, type_model=None, sub_type_model=None, condition_model=None, size_model=None, model_table=None, kilo_meter_model=None, transmission_type_model=None, rent_period_model=None, foul_type_model=None, internal_specs_model=None, outer_specs_model=None, regional_specs_model=None, car_number=None):
    ad = Car.objects.create(
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
        brand=brand_model,
        color=color_model,
        type=type_model,
        subtype=sub_type_model,
        condition=condition_model,
        size=size_model,
        model=model_table,
        transmission_type=transmission_type_model,
        foul_type=foul_type_model,
        kilo_meter=kilo_meter_model,
        rent_period=rent_period_model,
        internal_specs=internal_specs_model,
        outer_specs=outer_specs_model,
        regional_specs=regional_specs_model,
        car_number=car_number
    )
    return ad


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
    is_delivery = data.get("is_delivery")
    brand = data.get("brand")
    type = data.get("type")
    sub_type = data.get("sub_type")
    color = data.get("color")
    condition = data.get("condition")
    size = data.get('size')
    model = data.get('model')
    transmission_type = data.get('transmission_type')
    rent_period = data.get('rent_period')
    foul_type = data.get('foul_type')
    kilo_meter = data.get('kilo_meter')
    internal_specs = data.get('internal_specs')
    outer_specs = data.get('outer_specs')
    regional_specs = data.get('regional_specs')
    car_number = data.get('car_number')
    brand_model = None
    type_model = None
    sub_type_model = None
    condition_model = None
    color_model = None
    size_model = None
    model_table = None
    transmission_type_model = None
    rent_period_model = None
    foul_type_model = None
    kilo_meter_model = None
    internal_specs_model = None
    outer_specs_model = None
    regional_specs_model = None

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

    if brand:
        try:
            brand_model = Brand.objects.get(name=brand)
        except Brand.DoesNotExist:
            return Response({
                "message": "There's no brand with this name"
            }, status=status.HTTP_404_NOT_FOUND)

    if type:
        try:
            type_model = Type.objects.get(name=brand)
        except Type.DoesNotExist:
            return Response({
                "message": "There's no type with this name"
            }, status=status.HTTP_404_NOT_FOUND)

    if sub_type:
        try:
            sub_type_model = SubType.objects.get(name=brand)
        except SubType.DoesNotExist:
            return Response({
                "message": "There's no sub type with this name"
            }, status=status.HTTP_404_NOT_FOUND)

    if condition:
        try:
            condition_model = Condition.objects.get(name=brand)
        except Condition.DoesNotExist:
            return Response({
                "message": "There's no condition with this name"
            }, status=status.HTTP_404_NOT_FOUND)

    if color:
        try:
            color_model = Colors.objects.get(name=brand)
        except Colors.DoesNotExist:
            return Response({
                "message": "There's no color with this name"
            }, status=status.HTTP_404_NOT_FOUND)

    if size:
        try:
            size_model = Size.objects.get(name=size)
        except Size.DoesNotExist:
            return Response({
                "message": "There's no size with this name"
            }, status=status.HTTP_404_NOT_FOUND)

    if model:
        try:
            model_table = Model.objects.get(name=model)
        except Model.DoesNotExist:
            return Response({
                "message": "There's no model with this name"
            }, status=status.HTTP_404_NOT_FOUND)

    if kilo_meter:
        try:
            kilo_meter_model = KiloMeter.objects.get(name=kilo_meter)
        except KiloMeter.DoesNotExist:
            return Response({
                "message": "There's no kilo meter with this name"
            }, status=status.HTTP_404_NOT_FOUND)

    if transmission_type:
        try:
            transmission_type_model = TransmissionType.objects.get(
                name=transmission_type)
        except TransmissionType.DoesNotExist:
            return Response({
                "message": "There's no transmission type with this name"
            }, status=status.HTTP_404_NOT_FOUND)

    if rent_period:
        try:
            rent_period_model = RentPeriod.objects.get(name=rent_period)
        except RentPeriod.DoesNotExist:
            return Response({
                "message": "There's no rent period with this name"
            }, status=status.HTTP_404_NOT_FOUND)

    if internal_specs:
        for internal_spec in internal_specs:
            try:
                internal_specs_model = InternalSpecs.objects.get(
                    name=internal_spec)
            except InternalSpecs.DoesNotExist:
                return Response({
                    "message": "There's no internal specifications with this name"
                }, status=status.HTTP_404_NOT_FOUND)

    if outer_specs:
        try:
            outer_specs_model = OuterSpecs.objects.get(name=outer_specs)
        except OuterSpecs.DoesNotExist:
            return Response({
                "message": "There's no outer specifications with this name"
            }, status=status.HTTP_404_NOT_FOUND)

    if regional_specs:
        try:
            regional_specs_model = RegionalSpecs.objects.get(
                name=regional_specs)
        except RegionalSpecs.DoesNotExist:
            return Response({
                "message": "There's no regional specifications with this name"
            }, status=status.HTTP_404_NOT_FOUND)

    if foul_type:
        try:
            foul_type_model = FoulType.objects.get(name=foul_type)
        except FoulType.DoesNotExist:
            return Response({
                "message": "There's no foul type with this name"
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
                brand_model=brand_model,
                color_model=color_model,
                type_model=type_model,
                sub_type_model=sub_type_model,
                condition_model=condition_model,
                size_model=size_model,
                foul_type_model=foul_type_model,
                transmission_type_model=transmission_type_model,
                kilo_meter_model=kilo_meter_model,
                internal_specs_model=internal_specs_model,
                outer_specs_model=outer_specs_model,
                regional_specs_model=regional_specs_model,
                rent_period_model=rent_period_model,
                model_table=model_table,
                car_number=car_number,
            )
            add_images(ad, ad_images)
            update_ad_type(base_user_membership, ad)
            reward_user(user, ad)
            return Response({
                "message": "Congratulations! your ad is available now!"
            }, status=status.HTTP_400_BAD_REQUEST)
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
                brand_model=brand_model,
                color_model=color_model,
                type_model=type_model,
                sub_type_model=sub_type_model,
                condition_model=condition_model,
                size_model=size_model,
                foul_type_model=foul_type_model,
                transmission_type_model=transmission_type_model,
                kilo_meter_model=kilo_meter_model,
                internal_specs_model=internal_specs_model,
                outer_specs_model=outer_specs_model,
                regional_specs_model=regional_specs_model,
                rent_period_model=rent_period_model,
                model_table=model_table,
                car_number=car_number,
            )
            add_images(ad, ad_images)
            update_ad_type(membership, ad)
            reward_user(user, ad)
            return Response({
                "message": "Congratulations! your ad is available now!"
            }, status=status.HTTP_400_BAD_REQUEST)
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
                brand_model=brand_model,
                color_model=color_model,
                type_model=type_model,
                sub_type_model=sub_type_model,
                condition_model=condition_model,
                size_model=size_model,
                foul_type_model=foul_type_model,
                transmission_type_model=transmission_type_model,
                kilo_meter_model=kilo_meter_model,
                internal_specs_model=internal_specs_model,
                outer_specs_model=outer_specs_model,
                regional_specs_model=regional_specs_model,
                rent_period_model=rent_period_model,
                model_table=model_table,
                car_number=car_number,
            )
            add_images(ad, ad_images)
            return Response({
                "message": "Congratulations! your ad is available now!"
            }, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print(e)
            return Response({
                "message": "an error occurred while publishing your ad, please try again"
            }, status=status.HTTP_400_BAD_REQUEST)
