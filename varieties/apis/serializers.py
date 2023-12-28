from varieties import models
from rest_framework import serializers


class MechanismSerializer (serializers.ModelSerializer):
    class Meta:
        model = models.Mechanism
        fields = '__all__'


class Category (serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = '__all__'

    # def validate(self, attrs):
    #     name = attrs['name']

    #     if not name:
    #         raise serializers.ValidationError('Name can not be empty')

    #     if models.Category.objects.filter(name=name).exists():
    #         raise serializers.ValidationError('This name already exists')

    #     return super().validate(attrs)


class SubCategorySerializer (serializers.ModelSerializer):
    class Meta:
        model = models.SubCategory
        fields = '__all__'


class Brand (serializers.ModelSerializer):
    class Meta:
        model = models.Brand
        fields = '__all__'

    def validate(self, attrs):
        name = attrs['name']

        if not name:
            raise serializers.ValidationError('Name can not be empty')
        if models.Brand.objects.filter(name=name).exists():
            raise serializers.ValidationError('This name already exists')

        return super().validate(attrs)


class MaterialSerializer (serializers.ModelSerializer):
    class Meta:
        model = models.Material
        fields = '__all__'


class TypeSerializer (serializers.ModelSerializer):
    class Meta:
        model = models.Type
        fields = '__all__'


class Condition (serializers.ModelSerializer):
    class Meta:
        model = models.Condition
        fields = '__all__'

    def validate(self, attrs):
        name = attrs['name']

        if not name:
            raise serializers.ValidationError('Name can not be empty')

        if models.Condition.objects.filter(name=name).exists():
            raise serializers.ValidationError('This name already exists')

        return super().validate(attrs)


class SizeSerializer (serializers.ModelSerializer):
    class Meta:
        model = models.Size
        fields = '__all__'


class Colors (serializers.ModelSerializer):
    class Meta:
        model = models.Colors
        fields = '__all__'

    def validate(self, attrs):
        name = attrs['name']

        if not name:
            raise serializers.ValidationError('Name can not be empty')

        if models.Colors.objects.filter(name=name).exists():
            raise serializers.ValidationError('This name already exists')

        return super().validate(attrs)


class QualificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Qualification
        fields = '__all__'
    def create(self, validated_data):
        user = self.context['request'].user
        qualification = models.Qualification.objects.create(user=user, **validated_data)
        return qualification

class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Education
        fields = '__all__'


class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Experience
        fields = '__all__'
 

class PaymentMethodSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PaymentMethod
        fields = '__all__'


class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Currency
        fields = '__all__'


class CountrySerializer(serializers.ModelSerializer):
    # cities = serializers.StringRelatedField(many=True)

    class Meta:
        model = models.Country
        fields = '__all__'


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.City
        fields = '__all__'


class DefualtCitySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.City
        fields = ['name', "is_enabled"]


class AmenitySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Amenity
        fields = '__all__'


class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.SubCategory
        fields = "__all__"


class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Material
        fields = "__all__"


class TypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Type
        fields = "__all__"


class TopStyleSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TopStyle
        fields = ('name', 'is_enabled')


class SizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Size
        fields = "__all__"


class SubTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.SubType
        fields = "__all__"


class RentPeriodSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.RentPeriod
        fields = '__all__'


class CapacitySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Capacity
        fields = '__all__'


class KiloMeterSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.KiloMeter
        fields = '__all__'


class OSSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.OS
        fields = '__all__'


class MemorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Memory
        fields = '__all__'


class ModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Model
        fields = '__all__'


class StorageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Storage
        fields = '__all__'


class SubTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.SubType
        fields = '__all__'


class SiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Site
        fields = '__all__'
