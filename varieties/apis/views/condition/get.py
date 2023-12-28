from rest_framework import generics, mixins
from varieties.apis import serializers
from varieties.models import Condition

class GetCondition( generics.GenericAPIView, mixins.ListModelMixin ) :
    serializer_class = serializers.Condition
    queryset = Condition.objects.all()

    def get ( self, request ) : 
        return self.list( request )
    