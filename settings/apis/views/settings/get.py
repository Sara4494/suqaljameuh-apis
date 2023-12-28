from rest_framework.response import Response
from rest_framework import status, permissions, decorators
from settings.apis.serializers import SettingsSerializer
from django.shortcuts import get_object_or_404
from ....models import Settings

@decorators.api_view(["GET",])
def get_settings(request):
    try:
        setting = Settings.objects.get(pk=1)
        serializer = SettingsSerializer(setting, many=False).data
        return Response({
            "data": serializer
        }, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({
            "message": "an error occurred while getting the settings"
        }, status=status.HTTP_400_BAD_REQUEST)