from rest_framework import generics, mixins
from varieties.apis import serializers
from varieties.models import Condition
from rest_framework.permissions import IsAdminUser



class DeleteCondition ( generics.GenericAPIView, mixins.DestroyModelMixin ) :
    serializer_class = serializers.Condition
    queryset = Condition.objects.all()
    permission_classes = [IsAdminUser]


    def delete ( self, request, **args ) : 
        return self.destroy( request )
    