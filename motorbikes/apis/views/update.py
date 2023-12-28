from rest_framework.decorators import api_view, permission_classes, parser_classes
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.response import Response
from rest_framework import status
from django.core import exceptions
from users.permissions import UserActive, UserOwnerOnly
from varieties.models import SubCategory, Currency, Country, City, Type, PaymentMethod, KiloMeter, Capacity, Brand, Condition
from Ad.models import AdPicture
from education.models import Education


def add_images(ad, ad_images):
    for image in ad_images:
        AdPicture.objects.create(
            ad=ad,
            image=image
        )


def delete_images(ad, past_ad_images):
    for past_pic in past_ad_images:
        past_pic.delete()


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
    type = data.get("type")
    capacity = data.get("capacity")
    creation_year = data.get("creation_year")
    kilo_meter = data.get("kilo_meter")
    brand = data.get("brand")
    condition = data.get("condition")

    try:
        ad = Education.objects.get(pk=ad_id)
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
            ad.save()
            is_updated = True

        if country and ad.country.name != country:
            try:
                country_model = Country.objects.get(name=country)
            except Country.DoesNotExist:
                return Response({
                    "message": "this country doesn't exists"
                }, status=status.HTTP_404_NOT_FOUND)
            ad.country = country_model
            ad.save()
            is_updated = True

        if city and ad.city.name != city:
            try:
                city_model = City.objects.get(name=city)
            except City.DoesNotExist:
                return Response({
                    "message": "this city doesn't exists"
                }, status=status.HTTP_404_NOT_FOUND)
            ad.city = city_model
            ad.save()
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
            ad.save()
            is_updated = True

        if type and ad.type.name != type:
            try:
                type_model = Type.objects.get(name=type)
            except Type.DoesNotExist:
                return Response({
                    "message": "this type doesn't exists"
                }, status=status.HTTP_404_NOT_FOUND)
            ad.type = type_model
            ad.save()
            is_updated = True

        if capacity and ad.capacity.name != capacity:
            try:
                capacity_model = Capacity.objects.get(name=capacity)
            except Capacity.DoesNotExist:
                return Response({
                    "message": "this capacity doesn't exists"
                }, status=status.HTTP_404_NOT_FOUND)
            ad.capacity = capacity_model
            ad.save()
            is_updated = True

        if kilo_meter and ad.kilo_meter.name != kilo_meter:
            try:
                kilo_meter_model = KiloMeter.objects.get(name=kilo_meter)
            except KiloMeter.DoesNotExist:
                return Response({
                    "message": "this kilo meter doesn't exists"
                }, status=status.HTTP_404_NOT_FOUND)
            ad.kilo_meter = kilo_meter_model
            ad.save()
            is_updated = True

        if condition and ad.condition.name != condition:
            try:
                condition_model = Condition.objects.get(name=condition)
            except Condition.DoesNotExist:
                return Response({
                    "message": "this condition doesn't exists"
                }, status=status.HTTP_404_NOT_FOUND)
            ad.condition = condition_model
            ad.save()
            is_updated = True

        if brand and ad.brand.name != brand:
            try:
                brand_model = Brand.objects.get(name=brand)
            except Brand.DoesNotExist:
                return Response({
                    "message": "this brand doesn't exists"
                }, status=status.HTTP_404_NOT_FOUND)
            ad.brand = brand_model
            ad.save()
            is_updated = True

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
