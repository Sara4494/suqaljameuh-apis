from reports import models
from rest_framework import serializers
from comments.apis.serializers import AdCommentSerializer
from users.apis.serializers import UserSerializer
from Ad.apis.serializers import AdSerializer


class ReportAdSerializer(serializers.ModelSerializer):
    ad = AdSerializer(many=False)
    reported_by = UserSerializer(many=False)

    class Meta:
        model = models.ReportAd
        fields = '__all__'


class ReportProblemSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ReportProblem
        fields = '__all__'


class FavoritesSerializer(serializers.ModelSerializer):
    ad = AdSerializer(many=False, read_only=True)

    class Meta:
        model = models.Favorites
        fields = '__all__'


class ReportCommentSerializer (serializers.ModelSerializer):
    comment = AdCommentSerializer(many=False)
    report_by = UserSerializer(many=False)

    class Meta:
        model = models.ReportComment
        fields = '__all__'
