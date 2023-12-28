from rest_framework import serializers
from users.models import User
from user_profile.models import Profile
from user_profile.apis.serializer import ProfileSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from varieties.apis.serializers import CitySerializer, CountrySerializer
from memberships.models import UserMembership


class UserSerializer(serializers.ModelSerializer):
    city = CitySerializer(read_only=True, many=False)
    country = CountrySerializer(read_only=True, many=False)
    profile = serializers.SerializerMethodField(read_only=True)
    has_membership = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = ['id', 'full_name', 'email', 'password', 'phone_number',
                  'birth_date', 'joined_at', 'gender', 'city', 'country', "profile", "rate", "ratings_count", "is_online", "user_rank", "is_suspended", "verified", "followers", "followings", "has_membership"]

    def create(self, validated_data):

        email = validated_data['email']
        password = validated_data['password']

        data = validated_data

        data.pop('email')
        data.pop('password')

        user = User.objects.create_user(
            email=email, password=password, **data)

        return user

    def set_username(self, username):

        p = Profile.objects.get(user=self.user)

        p.username = username
        p.save()

    def get_jwt_tokens(self):

        refresh = RefreshToken.for_user(self.user)
        data = {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }

        return data

    def get_profile(self, obj):
        profile = obj.profile
        serializer = ProfileSerializer(profile, many=False)
        return serializer.data

    def get_has_membership(self, obj):
        return UserMembership.objects.filter(subscriber=obj).exists()


class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'full_name', 'email', 'password', 'phone_number',
                  'birth_date', 'joined_at', 'gender', 'city', 'country']

    def save(self, **kwargs):

        email = self.validated_data['email']
        password = self.validated_data['password']

        data = self.validated_data

        data.pop('email')
        data.pop('password')

        self.user = User.objects.create_superuser(
            email=email, password=password, **data)

        self.user.save()

    def set_username(self, username):

        p = Profile.objects.get(user=self.user)

        p.username = username
        p.save()

    def get_jwt_tokens(self):

        refresh = RefreshToken.for_user(self.user)
        data = {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }

        return data
