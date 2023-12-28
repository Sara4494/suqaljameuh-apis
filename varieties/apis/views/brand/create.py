from rest_framework import generics, mixins, serializers 
from varieties.apis import serializers
from rest_framework.permissions import IsAdminUser
from ....models import Brand, SubCategory
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status

class CreateBrand ( generics.GenericAPIView, mixins.CreateModelMixin ) :
    serializer_class = serializers.Brand
    permission_classes = [IsAdminUser]

    def post ( self, request ) : 

        return self.create( request )
    
