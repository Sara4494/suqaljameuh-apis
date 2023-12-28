from memberships.models import Membership, UserMembership, MembershipFeature, FeaturedMembership, FeaturedMembershipFeature, AdMembership, AdMembershipFeature
from users.apis.serializers import UserSerializer
from rest_framework import serializers


class FeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = MembershipFeature
        fields = "__all__"

class MembershipFeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeaturedMembershipFeature
        fields = "__all__"

class AdFeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeaturedMembershipFeature
        fields = "__all__"


class MembershipSerializer(serializers.ModelSerializer):
    features = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Membership
        fields = "__all__"

    def get_features(self, obj):
        membership_features = MembershipFeature.objects.filter(
            membership__id=obj.pk)
        serializer = FeatureSerializer(membership_features, many=True).data
        return serializer

class AdMembershipSerializer(serializers.ModelSerializer):
    features = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = AdMembership
        fields = "__all__"

    def get_features(self, obj):
        membership_features = AdMembershipFeature.objects.filter(
            membership__id=obj.pk)
        serializer = AdFeatureSerializer(membership_features, many=True).data
        return serializer


class FeaturedMembershipSerializer(serializers.ModelSerializer):
    features = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = FeaturedMembership
        fields = "__all__"

    def get_features(self, obj):
        membership_features = FeaturedMembershipFeature.objects.filter(
            membership__id=obj.pk)
        serializer = MembershipFeatureSerializer(membership_features, many=True).data
        return serializer

class UserMembershipSerializer(serializers.ModelField):
    subscriber = UserSerializer(many=False)
    membership = MembershipSerializer(many=False)

    class Meta:
        model = UserMembership
        fields = "__all__"
