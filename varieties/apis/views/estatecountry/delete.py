
# from rest_framework import status
# from rest_framework.decorators import api_view, permission_classes
# from rest_framework.response import Response
# from rest_framework.permissions import AllowAny, IsAdminUser
# from apartments.models import EstateCountry
# from apartments.apis.serializers import EstateCountrySerializer
# from django.utils.translation import gettext as _


# @api_view(['DELETE'])
# @permission_classes([IsAdminUser])
# def delete_estate_country(request, pk):
#     try:
#         estate_country = EstateCountry.objects.get(pk=pk)
#         estate_country.delete()
#         return Response({'message': _('EstateCountry deleted successfully.')}, status=status.HTTP_200_OK)
#     except EstateCountry.DoesNotExist:
#         return Response({'error': _('EstateCountry object not found.')}, status=status.HTTP_404_NOT_FOUND)
#     except Exception as e:
#         return Response({'error': str(e), 'message': _('Internal server error occurred.')}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
