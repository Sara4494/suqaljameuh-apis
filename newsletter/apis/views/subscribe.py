from rest_framework.decorators import api_view
from rest_framework.response import Response
from newsletter.apis.serializers import NewsletterSerializer
from newsletter.models import Newsletter
from rest_framework import status
@api_view(['POST'])
def subscribe(request):
    try:
        serializer = NewsletterSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            if Newsletter.objects.filter(email=email).exists():
                return Response({'message': 'This email is already registered at the newsletter'}, status=status.HTTP_400_BAD_REQUEST)
            serializer.save()
            return Response({'message': 'You have successfully subscribed for the newsletter'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({'message': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)