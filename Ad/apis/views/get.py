from rest_framework import decorators
from Ad.apis.serializers import AdPolymorphicSerializer
from Ad.models import Ad
from varieties.models import Category, SubCategory
from django.core import exceptions
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Case, When, Value
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


@decorators.api_view(['GET'])
def GetAllAds(request):
    try:
        ads = Ad.objects.all().order_by("-published_at")
        page = request.query_params.get("page")
        paginator = Paginator(ads, 10)

        if page == None or not page:
            page = 1
        page = int(page)

        try:
            ads = paginator.page(page)
        except PageNotAnInteger:
            ads = paginator.page(1)
        except EmptyPage:
            ads = paginator.page(paginator.num_pages)

        has_previous = ads.has_previous()
        has_next = ads.has_next()
        pages = paginator.num_pages

        serializer = AdPolymorphicSerializer(ads, many=True)
        return Response({
            "data": serializer.data,
            "page": page,
            "pages": pages,
            "has_previous": has_previous,
            "has_next": has_next,
        }, status=status.HTTP_200_OK)
    except Exception as e:
        print(e)
        return Response({
            "message": f"an error occurred while getting all the data"
        }, status=status.HTTP_400_BAD_REQUEST)


@decorators.api_view(["GET"])
def get__all(request):
    try:
        ads = Ad.objects.all()
        serializer = AdPolymorphicSerializer(ads, many=True)
        return Response({
            "data": serializer.data
        })
    except Exception as e:
        print(e)
        return Response({
            "data": "serializer.data"
        })


@decorators.api_view(['GET'])
def get_featured_ads(request):
    try:

        ads = Ad.objects.exclude(ad_type="Normal").order_by(
            Case(
                When(ad_type="Very Featured", then=Value(0)),
                When(ad_type="Featured", then=Value(1)),
                # default=Value(2)
            )
        )

        page = request.query_params.get("page")
        paginator = Paginator(ads, 10)

        if page == None or not page:
            page = 1
        page = int(page)

        try:
            ads = paginator.page(page)
        except PageNotAnInteger:
            ads = paginator.page(1)
        except EmptyPage:
            ads = paginator.page(paginator.num_pages)

        has_previous = ads.has_previous()
        has_next = ads.has_next()
        pages = paginator.num_pages

        serializer = AdPolymorphicSerializer(ads, many=True)
        print("Ads came2")
        return Response({
            "data": serializer.data,
            "page": page,
            "pages": pages,
            "has_previous": has_previous,
            "has_next": has_next,
        }, status=status.HTTP_200_OK)

    except Exception as e:
        return Response({
            "message": f"an error occurred while getting all the data : {e}"
        }, status=status.HTTP_400_BAD_REQUEST)


@decorators.api_view(["GET"])
def get_ad(request, ad_id):
    try:
        ad = Ad.objects.get(pk=ad_id)
    except exceptions.ObjectDoesNotExist:
        return Response({
            "message": "This Ad Doesn't Exists Or Maybe The Publisher Deleted It"
        }, status=status.HTTP_404_NOT_FOUND)

    try:
        ad_serializer = AdPolymorphicSerializer(ad, many=False).data
        print(ad_serializer)
        return Response({
            "data": ad_serializer,
        }, status=status.HTTP_200_OK)
    except Exception as e:
        print(e)
        return Response({
            "message": "An error occurred while retrieving the information of the ad"
        }, status=status.HTTP_400_BAD_REQUEST)


@decorators.api_view(["GET"])
def get_user_ads(request):
    try:
        ads = Ad.objects.filter(user=request.user)
        page = request.query_params.get("page")
        paginator = Paginator(ads, 10)

        if page == None or not page:
            page = 1
        page = int(page)

        try:
            ads = paginator.page(page)
        except PageNotAnInteger:
            ads = paginator.page(1)
        except EmptyPage:
            ads = paginator.page(paginator.num_pages)

        has_previous = ads.has_previous()
        has_next = ads.has_next()
        pages = paginator.num_pages
        active_ads = Ad.objects.filter(user=request.user, active=True).count()
        inactive_ads = Ad.objects.filter(user=request.user, active=False).count()

        serializer = AdPolymorphicSerializer(ads, many=True)
        return Response({
            "data": serializer.data,
            "page": page,
            "pages": pages,
            "has_previous": has_previous,
            "has_next": has_next,
            "active_ads": active_ads,
            "inactive_ads": inactive_ads
        }, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({
            "message": "An error occurred while retrieving the information of the ad"
        }, status=status.HTTP_400_BAD_REQUEST)


@decorators.api_view(["GET"])
def get_seller_ads(request, user_id):
    try:
        ads = Ad.objects.filter(user__id=user_id)
        ad_serializer = AdPolymorphicSerializer(ads, many=True).data
        return Response({
            "data": ad_serializer
        }, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({
            "message": "An error occurred while retrieving the information of the ad"
        }, status=status.HTTP_400_BAD_REQUEST)


@decorators.api_view(["GET"])
def get_category_ads(request, category_name):
    try:
        category = Category.objects.get(name=category_name)
    except Category.DoesNotExist:
        return Response({
            "message": "Cannot find this category"
        }, status=status.HTTP_404_NOT_FOUND)

    try:
        ads = Ad.objects.filter(category__category=category)
        page = request.query_params.get("page")
        paginator = Paginator(ads, 10)

        if page == None or not page:
            page = 1
        page = int(page)

        try:
            ads = paginator.page(page)
        except PageNotAnInteger:
            ads = paginator.page(1)
        except EmptyPage:
            ads = paginator.page(paginator.num_pages)

        has_previous = ads.has_previous()
        has_next = ads.has_next()
        pages = paginator.num_pages

        serializer = AdPolymorphicSerializer(ads, many=True)
        return Response({
            "data": serializer.data,
            "page": page,
            "pages": pages,
            "has_previous": has_previous,
            "has_next": has_next,
        }, status=status.HTTP_200_OK)
    except Exception as e:
        print(e)
        return Response({
            "message": "An error occurred while retrieving the information of the ad"
        }, status=status.HTTP_400_BAD_REQUEST)


@decorators.api_view(["GET"])
def get_related_ads(request, ad_id, subcategory_id):
    try:
        subcategory = SubCategory.objects.get(pk=subcategory_id)
    except Category.DoesNotExist:
        return Response({
            "message": "Cannot find this subcategory"
        }, status=status.HTTP_404_NOT_FOUND)

    try:
        ads = Ad.objects.exclude(pk=ad_id).filter(category=subcategory)
        page = request.query_params.get("page")
        paginator = Paginator(ads, 10)

        if page == None or not page:
            page = 1
        page = int(page)

        try:
            ads = paginator.page(page)
        except PageNotAnInteger:
            ads = paginator.page(1)
        except EmptyPage:
            ads = paginator.page(paginator.num_pages)

        has_previous = ads.has_previous()
        has_next = ads.has_next()
        pages = paginator.num_pages

        serializer = AdPolymorphicSerializer(ads, many=True)
        return Response({
            "data": serializer.data,
            "page": page,
            "pages": pages,
            "has_previous": has_previous,
            "has_next": has_next,
        }, status=status.HTTP_200_OK)
    except Exception as e:
        print(e)
        return Response({
            "message": "An error occurred while retrieving the information of the ad"
        }, status=status.HTTP_400_BAD_REQUEST)
