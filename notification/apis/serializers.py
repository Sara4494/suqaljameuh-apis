
from notification.models import Notification, NotificationSettings
from rest_framework import serializers


class NotificationSerializer (serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = '__all__'


class NotificationSettingSerializer (serializers.ModelSerializer):
    class Meta:
        model = NotificationSettings
        fields = '__all__'
