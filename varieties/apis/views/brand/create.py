from rest_framework import generics, mixins, serializers as sr
from varieties.apis import serializers
from rest_framework.permissions import IsAdminUser
from ....models import Brand

class CreateBrand ( generics.GenericAPIView, mixins.CreateModelMixin ) :
    serializer_class = serializers.Brand
    permission_classes = [IsAdminUser]

    def post ( self, request ) : 

        return self.create( request )
    

