from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import permissions, status
from varieties.models import Country
from varieties.apis.serializers import CountrySerializer
@api_view(['PUT'])
@permission_classes([permissions.IsAdminUser])
def update_country(request, pk):
    try:
        country = Country.objects.get(pk=pk)
        serializer = CountrySerializer(country, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Country updated successfully.', 'data': serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Country.DoesNotExist:
        return Response({'error': 'Country object not found.'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
