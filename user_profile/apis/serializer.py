from rest_framework import serializers
from ..models import Profile

class ProfileSerializer(serializers.ModelSerializer) : 
    
    
    class Meta : 
        model = Profile
        exclude = ('user',)


    def validate(self, attrs):


        if 'facebook_acc' in attrs : 
            facebook_acc = attrs['facebook_acc']
            
            if  facebook_acc is not None and '.facebook.com' not in facebook_acc :
                raise serializers.ValidationError('Invalid facebook account')
        
        if 'instagram_acc' in attrs : 
            instagram_acc = attrs['instagram_acc']
            if instagram_acc is not None and '.instagram.com' not in instagram_acc :
                raise serializers.ValidationError('Invalid instagram account')

        return super().validate(attrs)

    