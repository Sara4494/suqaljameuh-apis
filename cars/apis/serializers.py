from rest_framework import serializers
from cars.models import Car, TransmissionType,OuterSpecs, BodyType, FoulType, InternalSpecs, RegionalSpecs


class TransmissionTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransmissionType
        fields = "__all__"


class BodyTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = BodyType
        fields = "__all__"


class FoulTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoulType
        fields = "__all__"


class FoulTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoulType
        fields = "__all__"


class InternalSpecsSerializer(serializers.ModelSerializer):
    class Meta:
        model = InternalSpecs
        fields = "__all__"


class RegionalSpecsSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegionalSpecs
        fields = "__all__"


class OuterSpecsSerializer(serializers.ModelSerializer):
    class Meta:
        model = OuterSpecs
        fields = "__all__"