from rest_framework import decorators, status
from .models import Brand, Material, TopStyle
from rest_framework.response import Response


@decorators.api_view(['GET'])
def Retrievefilters(request) : 


    response = {
        'brand' :Brand.objects.all().values('name','added_at'),
        'material' :Material.objects.all().values('name','added_at'),
        'top_style' :TopStyle.objects.all().values('name','added_at'),
    }

    return Response(data=response,status=status.HTTP_200_OK)