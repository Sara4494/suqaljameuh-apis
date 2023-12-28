from rest_framework import generics, mixins
from varieties.apis import serializers
from varieties.models import Category

class GetCategory ( generics.GenericAPIView, mixins.ListModelMixin ) :
    serializer_class = serializers.Category
    queryset = Category.objects.all()

    def get ( self, request ) : 
        return self.list( request )
    