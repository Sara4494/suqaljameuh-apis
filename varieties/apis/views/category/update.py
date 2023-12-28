from rest_framework import generics, mixins
from rest_framework.response import Response
from varieties.apis import serializers
from varieties.models import Category
from rest_framework.permissions import IsAdminUser

class UpdateCategory ( generics.GenericAPIView, mixins.UpdateModelMixin , mixins.RetrieveModelMixin) :
    serializer_class = serializers.Category
    queryset = Category.objects.all()
    permission_classes = [IsAdminUser]

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
    

    def put ( self, request , **args ) : 
        return self.update( request )
    
