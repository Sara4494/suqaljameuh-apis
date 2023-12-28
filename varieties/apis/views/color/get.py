from rest_framework import generics, mixins
from varieties.apis import serializers
from varieties.models import Colors

class GetColor ( generics.GenericAPIView, mixins.ListModelMixin ) :
    serializer_class = serializers.Colors
    queryset = Colors.objects.all()

    def get ( self, request ) : 
        return self.list( request )
    