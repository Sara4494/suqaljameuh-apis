from rest_framework import generics, mixins
from varieties.apis import serializers
from varieties.models import Colors
from rest_framework.permissions import IsAdminUser


class DeleteColor ( generics.GenericAPIView, mixins.DestroyModelMixin ) :
    serializer_class = serializers.Colors
    queryset = Colors.objects.all()
    permission_classes = [IsAdminUser]


    def delete ( self, request, **args ) : 
        return self.destroy( request )
    