from rest_framework import serializers
from comments.models import AdComment
from Ad.apis.serializers import AdSerializer
from users.apis.serializers import UserSerializer
from user_profile.models import Profile
from user_profile.apis.serializer import ProfileSerializer


class AdCommentSerializer(serializers.ModelSerializer):
    ad = AdSerializer(read_only=True, many=False)
    user = UserSerializer(read_only=True, many=False)
    user_profile = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = AdComment
        fields = "__all__"

    def get_user_profile(self, obj):
        profile = Profile.objects.get(user=obj.user)
        serializer = ProfileSerializer(profile, many=False)
        return serializer.data

