from reports import models
from rest_framework import serializers
 
class ReportAdSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ReportAd
        fields = '__all__'