from rest_framework import serializers
from apartments.models import NearLocation, AdjustedTo, Interface, RoomCounts, BathroomCounts, FloorsCounts, BuildingAge, AdditionalFeature, EstateType, RealEstate
from varieties.apis.serializers import AmenitySerializer
from varieties.models import Country


class NearLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = NearLocation
        fields = "__all__"


class AdjustedToSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdjustedTo
        fields = "__all__"


class InterfaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interface
        fields = "__all__"


class RoomCountsSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoomCounts
        fields = "__all__"


class FloorsCountsSerializer(serializers.ModelSerializer):
    class Meta:
        model = FloorsCounts
        fields = "__all__"


class BathroomCountsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BathroomCounts
        fields = "__all__"


class BuildingAgeSerializer(serializers.ModelSerializer):
    class Meta:
        model = BuildingAge
        fields = "__all__"


class AdditionalFeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdditionalFeature
        fields = "__all__"


class EstateTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EstateType
        fields = "__all__"


class EstateCountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = "__all__"