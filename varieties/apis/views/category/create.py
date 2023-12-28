from rest_framework import generics, mixins
from varieties.apis import serializers
from rest_framework.permissions import IsAdminUser



class CreateCategory ( generics.GenericAPIView, mixins.CreateModelMixin ) :
    serializer_class = serializers.Category
    permission_classes = [IsAdminUser]

    def post ( self, request ) : 
        return self.create( request )