
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import permissions, status
from varieties.models import Education
from varieties.apis.serializers import EducationSerializer
@api_view(['PUT'])
@permission_classes([permissions.IsAuthenticated])
def education_update(request, pk):
    try:
        education = Education.objects.get(pk=pk, user=request.user)
        serializer = EducationSerializer(education, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Education updated successfully.', 'data': serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Education.DoesNotExist:
        return Response({'error': 'Education object not found.'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
