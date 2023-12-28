from celery import shared_task
from django.core.mail import send_mail
from newsletter.models import Newsletter
from django.http import HttpResponse
from newsletter.apis.serializers import *
from newsletter.models import Newsletter
from django.core.mail import send_mail
from rest_framework import status
from django.conf import settings

@shared_task
def send_top_rated_news(request):
    try:
        # Get all subscribed users
        newsletters = Newsletter.objects.all()

        # Send email to each user
        for newsletter in newsletters:
            send_mail(
                'Top Rated News',
                'Here are the top rated news of the week',
                settings.EMAIL_HOST_USER,
                [newsletter.email],
                fail_silently=True,
            )
        return HttpResponse('Top rated news sent successfully', status=status.HTTP_200_OK)
    except Exception as e:
        return HttpResponse('An error occurred while sending the top rated news', status=status.HTTP_500_INTERNAL_SERVER_ERROR)