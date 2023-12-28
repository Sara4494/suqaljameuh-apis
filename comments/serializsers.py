from rest_framework import serializers
from .models import AdComment


class AdCommentSerializer (serializers.ModelSerializer) : 
    class Meta : 
        model = AdComment
        fields = '__all__'