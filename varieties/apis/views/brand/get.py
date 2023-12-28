from rest_framework import generics, mixins
from varieties.apis import serializers
from varieties.models import Brand

class GetBrand ( generics.GenericAPIView, mixins.ListModelMixin ) :
    serializer_class = serializers.Brand
    queryset = Brand.objects.all()

    def get ( self, request ) : 
        return self.list( request )
    