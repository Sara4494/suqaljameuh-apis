from rest_framework import generics, mixins
from varieties.apis import serializers
from varieties.models import Condition
from rest_framework.response import Response
from rest_framework import status

class GetCondition( generics.GenericAPIView, mixins.ListModelMixin ) :
    serializer_class = serializers.Condition
    queryset = Condition.objects.all()

    def get ( self, request ) : 
        return self.list( request )
    

def get_conditions(request, subcategory_id):
    try:
        conditions = Condition.objects.filter(category__id=subcategory_id)
        serializer = serializers.Condition(conditions, many=True)
        return Response({
            "data": serializer.data
        }, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({
            "message": "an error occurred while getting conditions"
        }, status=status.HTTP_400_BAD_REQUEST)