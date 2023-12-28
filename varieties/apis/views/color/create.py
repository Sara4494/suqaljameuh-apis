from rest_framework import generics, mixins
from varieties.apis import serializers
from rest_framework.permissions import IsAdminUser



class CreateColor ( generics.GenericAPIView, mixins.CreateModelMixin ) :
    serializer_class = serializers.Colors
    permission_classes = [IsAdminUser]

    def post ( self, request ) : 
        return self.create( request )