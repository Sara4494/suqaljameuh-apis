from rest_framework.response import Response
from rest_framework import status, permissions, decorators
from settings.apis.serializers import PageSerializer
from django.shortcuts import get_object_or_404
from ....models import Page

@decorators.api_view(["GET"])
@decorators.permission_classes([permissions.IsAdminUser])
def get_pages(request):
    try:
        pages = Page.objects.all()
        serializer = PageSerializer(pages, many=True)
        return Response({
            "data": serializer.data
        }, status=status.HTTP_200_OK)
    except Exception as e:
        print(e)
        return Response({
            "message": "an error while getting pages"
        }, status=status.HTTP_400_BAD_REQUEST)

@decorators.api_view(["GET"])
@decorators.permission_classes([permissions.IsAdminUser])
def get_page(request, page_id):
    try:
        page = Page.objects.get(pk=page_id)
    except Page.DoesNotExist:
        return Response({
            "message": "Sorry, We cannot find the page you requested"
        }, status=status.HTTP_404_NOT_FOUND)
    
    try:
        serializer = PageSerializer(page, many=False)
        return Response({
            "data": serializer.data
        }, status=status.HTTP_200_OK)
    except Exception as e:
        print(e)
        return Response({
            "message": "an error while getting the page"
        }, status=status.HTTP_400_BAD_REQUEST)