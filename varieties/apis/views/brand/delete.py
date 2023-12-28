from rest_framework import generics, mixins
from varieties.apis import serializers
from varieties.models import Brand
from rest_framework.permissions import IsAdminUser



class DeleteBrand ( generics.GenericAPIView, mixins.DestroyModelMixin ) :
    permission_classes = [IsAdminUser]
    serializer_class = serializers.Brand
    queryset = Brand.objects.all()



    def delete ( self, request , **args) : 
        return self.destroy( request )
    