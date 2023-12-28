from rest_framework.response import Response
from rest_framework import status, permissions, decorators
from settings.apis.serializers import SettingsSerializer
from django.shortcuts import get_object_or_404
from ....models import Settings

@decorators.api_view(['PUT'])
@decorators.permission_classes([permissions.IsAdminUser])
def UpdateSettings (request, settingid) : 

    settings = get_object_or_404(Settings,id = settingid)

    try : 
        
        serializer = SettingsSerializer(settings,data=request.data)

        if serializer.is_valid() : 
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    except Exception as error : 
        return Response({'message':f'An error accured : {error}'},status=status.HTTP_400_BAD_REQUEST)