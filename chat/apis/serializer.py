from rest_framework import serializers
from chat.models import Chat, Message
from users.apis.serializers import UserSerializer


class ChatSerializer (serializers.ModelSerializer):
    users = UserSerializer(many=True, read_only=True)
    last_sender = UserSerializer(many=False, read_only=True)
    class Meta:
        model = Chat
        fields = "__all__"


class MessageSerializer (serializers.ModelSerializer):
    sender = UserSerializer(many=False, read_only=True)
    class Meta:
        model = Message
        fields = "__all__"

class AdminMessageSerializer (serializers.ModelSerializer):
    sender = UserSerializer(many=False, read_only=True)
    chat = ChatSerializer(many=False, read_only=True)
    class Meta:
        model = Message
        fields = "__all__"
