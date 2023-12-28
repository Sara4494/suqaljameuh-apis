
# from rest_framework import status
# from rest_framework.decorators import api_view, permission_classes
# from rest_framework.response import Response
# from rest_framework.permissions import AllowAny, IsAdminUser
# from apartments.models import EstateCountry
# from apartments.apis.serializers import EstateCountrySerializer
# from django.utils.translation import gettext as _


# @api_view(['PUT'])
# @permission_classes([IsAdminUser])
# def update_estate_country(request, pk):
#     try:
#         estate_country = EstateCountry.objects.get(pk=pk)
#     except EstateCountry.DoesNotExist:
#         return Response({'error': _('EstateCountry does not exist')}, status=status.HTTP_404_NOT_FOUND)

#     try:
#         name = request.data.get('name')
#         if name and EstateCountry.objects.filter(name=name).exclude(pk=pk).exists():
#             return Response({'error': _('This name is already registered at the EstateCountry.')}, status=status.HTTP_400_BAD_REQUEST)
#         serializer = EstateCountrySerializer(estate_country, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'success': _('EstateCountry updated successfully')}, status=status.HTTP_200_OK)
#         return Response({'error': _('Invalid data provided')}, status=status.HTTP_400_BAD_REQUEST)
#     except Exception as e:
#         return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
