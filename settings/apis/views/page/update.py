from rest_framework.response import Response
from rest_framework import status, permissions, decorators
from settings.apis.serializers import PageSerializer
from django.shortcuts import get_object_or_404
from ....models import Page

@decorators.api_view(['PUT'])
@decorators.permission_classes([permissions.IsAdminUser])
def UpdatePage (request, pageid) : 

    page = get_object_or_404(Page,id = pageid)

    try : 

        if 'slug' in request.data : 
            return Response({'message':'you can not update slug field !'}, status=status.HTTP_400_BAD_REQUEST)

        serializer = PageSerializer(page,data=request.data)

        if serializer.is_valid() : 
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    except Exception as error : 
        return Response({'message':f'An error accured : {error}'},status=status.HTTP_400_BAD_REQUEST)