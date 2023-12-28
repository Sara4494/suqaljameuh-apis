from rest_framework.decorators import api_view, permission_classes, parser_classes
from rest_framework.response import Response
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework import status
from education.models import Education
from users.permissions import UserActive
from memberships.models import AdMembership, UserMembership
from varieties.models import SubCategory, Currency, Country, City, Type, PaymentMethod, Site
from Ad.models import AdPicture
from globals.payment_helpers import create_charge, create_customer
from globals.global_tasks import reward_user
from globals.ad_helpers import update_ad_type
from django.conf import settings

import stripe
stripe.api_key = settings.STRIPE_PRIVATE_KEY


def create_ad(user, sub_category, title, description, country_model, city_model, currency_model, payment_method_model, price, full_name=None, phone_number=None, lat=None, lat_delta=None, long=None, long_delta=None, type_model=None, site_model=None):
    ad = Education.objects.create(
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
        type=type_model,
        site=site_model
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
def publish_education_ad(request):
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
    type = data.get("type")
    site = data.get("site")

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
            "message": "Please enter payment method"
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

    if not type:
        return Response({
            "message": "Please enter the type"
        }, status=status.HTTP_400_BAD_REQUEST)

    try:
        type_model = Type.objects.get(name=type)
    except Type.DoesNotExist:
        return Response({
            "message": "There's no type with this name"
        }, status=status.HTTP_404_NOT_FOUND)

    if not site:
        return Response({
            "message": "Please enter the site"
        }, status=status.HTTP_400_BAD_REQUEST)

    try:
        site_model = Site.objects.get(name=site)
    except Site.DoesNotExist:
        return Response({
            "message": "There's no site with this name"
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
            ad = create_ad(user=user,
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
                           site_model=site_model,
                           type_model=type_model
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
            ad = create_ad(user=user,
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
                           site_model=site_model,
                           type_model=type_model
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
            ad = create_ad(user=user,
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
                           site_model=site_model,
                           type_model=type_model
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
