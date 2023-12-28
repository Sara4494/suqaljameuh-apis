from rest_framework import serializers
from ..models import Page, Settings



class PageSerializer (serializers.ModelSerializer) : 
    class Meta :
        model = Page
        fields = '__all__'


class SettingsSerializer (serializers.ModelSerializer) : 
    class Meta : 
        model = Settings
        fields = '__all__'