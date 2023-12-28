from rest_framework.decorators import api_view, permission_classes, parser_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import FormParser, MultiPartParser
from users.permissions import UserActive
from memberships.models import AdMembership, UserMembership
from varieties.models import SubCategory, Currency, Country, City, Brand, Type, Size, Colors, Condition, PaymentMethod
from Ad.models import AdPicture, Ad, RateAd
from globals.payment_helpers import create_charge, create_customer
from globals.global_tasks import reward_user
from globals.ad_helpers import update_ad_type
from django.conf import settings
from django.core import exceptions

import stripe
stripe.api_key = settings.STRIPE_PRIVATE_KEY


def create_ad(user, sub_category, title, description, country_model, city_model, currency_model, payment_method_model, price, full_name=None, phone_number=None, lat=None, lat_delta=None, long=None, long_delta=None, is_delivery=False, brand_model=None, color_model=None, type_model=None, condition_model=None, size_model=None):
    ad = Ad.objects.create(
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
        condition=condition_model,
        size=size_model
    )
    return ad


def add_images(ad, ad_images):
    print("printed from add_images", ad_images)
    for image in ad_images:
        print("image before creation:", image)
        image_after_created = AdPicture.objects.create(
            ad=ad,
            image=image
        )
        print("image after creation:", image_after_created.image)


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
    ad_images = request.FILES.getlist('ad_images')
    payment_method = data.get("payment_method")
    lat = data.get("lat")
    lat_delta = data.get("lat_delta")
    long_delta = data.get("long_delta")
    long = data.get("long")
    membership_name = data.get("membership_name")
    full_name = data.get("full_name")
    phone_number = data.get("phone_number")
    is_delivery = bool(data.get("is_delivery"))
    brand = data.get("brand")
    type = data.get("type")
    color = data.get("color")
    condition = data.get("condition")
    size = data.get('size')
    brand_model = None
    type_model = None
    condition_model = None
    color_model = None
    size_model = None

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
            type_model = Type.objects.get(name=type)
        except Type.DoesNotExist:
            return Response({
                "message": "There's no type with this name"
            }, status=status.HTTP_404_NOT_FOUND)

    if condition:
        try:
            condition_model = Condition.objects.get(name=condition)
        except Condition.DoesNotExist:
            return Response({
                "message": "There's no condition with this name"
            }, status=status.HTTP_404_NOT_FOUND)

    if color:
        try:
            color_model = Colors.objects.get(name=color)
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
                condition_model=condition_model,
                size_model=size_model)
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
                brand_model=brand_model,
                color_model=color_model,
                type_model=type_model,
                condition_model=condition_model,
                size_model=size_model
            )
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
                brand_model=brand_model,
                color_model=color_model,
                type_model=type_model,
                condition_model=condition_model,
                size_model=size_model
            )
            add_images(ad, ad_images)
            return Response({
                "message": "Congratulations! your ad is available now!"
            }, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response({
                "message": "an error occurred while publishing your ad, please try again"
            }, status=status.HTTP_400_BAD_REQUEST)

@api_view(["POST"])
@permission_classes([UserActive])
def rate_ad(request, ad_id):
    data = request.data
    user = request.user

    if not data:
        return Response({
            "message": "Please enter the needed data"
        }, status=status.HTTP_400_BAD_REQUEST)
    
    try:
        ad = Ad.objects.get(pk=ad_id)
    except exceptions.ObjectDoesNotExist:
        return Response({
            "message": "The ad you're trying to rate isn't available"
        }, status=status.HTTP_404_NOT_FOUND)
    
    rating = data.get('rating')

    rating_exists = RateAd.objects.filter(ad=ad, user=user).exists()

    if rating_exists:
        return Response({
            "message": "You already have rated this ad one time before"
        }, status=status.HTTP_400_BAD_REQUEST)

    try:
        RateAd.objects.create(ad=ad, user=user, rate=rating)
        
        ratings = ad.ad_ratings.all()
        ad.ratings_count = len(ratings)
        total = 0

        for i in ratings:
            total = i.rate
        
        ad.rating = total / len(ratings)
        ad.save()
        return Response({
            "data": f"You have rated {ad.ad_title}"
        }, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({
            "message": f"An error occurred while creating the review {e}"
        }, status=status.HTTP_400_BAD_REQUEST)