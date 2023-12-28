from rest_framework import generics, mixins, status
from rest_framework.response import Response
from varieties.apis import serializers
from varieties.models import Brand

class GetBrand ( generics.GenericAPIView, mixins.ListModelMixin ) :
    serializer_class = serializers.Brand
    queryset = Brand.objects.all()

    def get ( self, request ) : 
        return self.list( request )

def get_brands(request, subcategory_id):
    try:
        brands = Brand.objects.filter(category__id=subcategory_id)
        serializer = serializers.Brand(brands, many=True)
        return Response({
            "data": serializer.data
        }, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({
            "message": "an error occurred while getting brands"
        }, status=status.HTTP_400_BAD_REQUEST)