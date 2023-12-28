from rest_framework import generics, mixins
from varieties.apis import serializers
from varieties.models import Category
from rest_framework.permissions import IsAdminUser



class DeleteCategory ( generics.GenericAPIView, mixins.DestroyModelMixin ) :
    serializer_class = serializers.Category
    queryset = Category.objects.all()
    permission_classes = [IsAdminUser]


    def delete ( self, request, **args ) : 
        return self.destroy( request )
    