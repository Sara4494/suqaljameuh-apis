from rest_framework import serializers
from ..models import Ad, AdPicture
from menfashion.models import Fashion
from education.models import Education
from motorbikes.models import MotorBikes
from electronics.models import Electronics
from apartments.apis.serializers import NearLocationSerializer, AdjustedToSerializer, AdditionalFeatureSerializer, EstateTypeSerializer, EstateCountrySerializer
from apartments.models import RealEstate
from varieties.apis.serializers import AmenitySerializer
from cars.models import Car
from rest_polymorphic.serializers import PolymorphicSerializer
from varieties.apis.serializers import Brand, Colors, TypeSerializer, MaterialSerializer, ModelSerializer, TopStyleSerializer, Condition, SizeSerializer, CountrySerializer, CitySerializer, CurrencySerializer, PaymentMethodSerializer
from users.apis.serializers import UserSerializer
from computers.models import Computer
from varieties.apis.serializers import MechanismSerializer, SubTypeSerializer


class AdPictureSerializer(serializers.ModelSerializer):
    # ad_images = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = AdPicture
        fields = "__all__"

    # def get_ad_images(self, obj):
    #     ad_images = AdPicture.objects.filter(ad__id=obj.pk)
    #     serializer = AdPictureSerializer(ad_images, many=True).data
    #     return serializer


class EducationSerializer(serializers.ModelSerializer):
    ad_images = serializers.SerializerMethodField(read_only=True)
    user = UserSerializer(many=False)
    country = CountrySerializer(many=False, read_only=True)
    city = CitySerializer(many=False, read_only=True)
    currency = CurrencySerializer(many=False, read_only=True)
    payment_method = PaymentMethodSerializer(many=False, read_only=True)

    class Meta:
        model = Education
        fields = "__all__"

    def get_ad_images(self, obj):
        ad_images = AdPicture.objects.filter(ad__id=obj.pk)
        serializer = AdPictureSerializer(ad_images, many=True).data
        return serializer


class ElectronicsSerializer(serializers.ModelSerializer):
    ad_images = serializers.SerializerMethodField(read_only=True)
    user = UserSerializer(many=False)
    country = CountrySerializer(many=False, read_only=True)
    city = CitySerializer(many=False, read_only=True)
    currency = CurrencySerializer(many=False, read_only=True)
    payment_method = PaymentMethodSerializer(many=False, read_only=True)

    class Meta:
        model = Electronics
        fields = "__all__"

    def get_ad_images(self, obj):
        ad_images = AdPicture.objects.filter(ad__id=obj.pk)
        serializer = AdPictureSerializer(ad_images, many=True).data
        return serializer


class FashionSerializer(serializers.ModelSerializer):
    mechanism = MechanismSerializer(many=False, read_only=True)
    subtype = SubTypeSerializer(many=False, read_only=True)
    ad_images = serializers.SerializerMethodField(read_only=True)
    user = UserSerializer(many=False)
    country = CountrySerializer(many=False, read_only=True)
    city = CitySerializer(many=False, read_only=True)
    currency = CurrencySerializer(many=False, read_only=True)
    payment_method = PaymentMethodSerializer(many=False, read_only=True)

    class Meta:
        model = Fashion
        fields = "__all__"

    def get_ad_images(self, obj):
        ad_images = AdPicture.objects.filter(ad__id=obj.pk)
        serializer = AdPictureSerializer(ad_images, many=True).data
        return serializer


class ComputerSerializer(serializers.ModelSerializer):
    ad_images = serializers.SerializerMethodField(read_only=True)
    user = UserSerializer(many=False)
    country = CountrySerializer(many=False, read_only=True)
    city = CitySerializer(many=False, read_only=True)
    currency = CurrencySerializer(many=False, read_only=True)
    payment_method = PaymentMethodSerializer(many=False, read_only=True)

    class Meta:
        model = Computer
        fields = "__all__"

    def get_ad_images(self, obj):
        ad_images = AdPicture.objects.filter(ad__id=obj.pk)
        serializer = AdPictureSerializer(ad_images, many=True).data
        return serializer


class CarSerializer(serializers.ModelSerializer):
    ad_images = serializers.SerializerMethodField(read_only=True)
    user = UserSerializer(many=False)
    country = CountrySerializer(many=False, read_only=True)
    city = CitySerializer(many=False, read_only=True)
    currency = CurrencySerializer(many=False, read_only=True)
    payment_method = PaymentMethodSerializer(many=False, read_only=True)

    class Meta:
        model = Car
        fields = "__all__"

    def get_ad_images(self, obj):
        ad_images = AdPicture.objects.filter(ad__id=obj.pk)
        serializer = AdPictureSerializer(ad_images, many=True).data
        return serializer


class MotorBikesSerializer(serializers.ModelSerializer):
    ad_images = serializers.SerializerMethodField(read_only=True)
    user = UserSerializer(many=False)
    country = CountrySerializer(many=False, read_only=True)
    city = CitySerializer(many=False, read_only=True)
    currency = CurrencySerializer(many=False, read_only=True)
    payment_method = PaymentMethodSerializer(many=False, read_only=True)

    class Meta:
        model = MotorBikes
        fields = "__all__"

    def get_ad_images(self, obj):
        ad_images = AdPicture.objects.filter(ad__id=obj.pk)
        serializer = AdPictureSerializer(ad_images, many=True).data
        return serializer


class RealStateSerializer(serializers.ModelSerializer):
    near_location = NearLocationSerializer(many=False, read_only=True)
    adjusted_to = AdjustedToSerializer(many=False, read_only=True)
    # interface = InterfaceSerializer(many=False, read_only=True)
    # room_counts = RoomCountsSerializer(many=False, read_only=True)
    # bathroom_counts = BathroomCountsSerializer(many=False, read_only=True)
    # floors_counts = FloorsCountsSerializer(many=False, read_only=True)
    # building_age = BuildingAgeSerializer(many=False, read_only=True)
    additional_features = AdditionalFeatureSerializer(
        many=True, read_only=True)
    amenities = AmenitySerializer(many=True, read_only=True)
    estate_country = EstateCountrySerializer(many=False, read_only=True)
    estate_type = EstateTypeSerializer(many=False, read_only=True)
    ad_images = serializers.SerializerMethodField(read_only=True)
    user = UserSerializer(many=False)
    country = CountrySerializer(many=False, read_only=True)
    city = CitySerializer(many=False, read_only=True)
    currency = CurrencySerializer(many=False, read_only=True)
    payment_method = PaymentMethodSerializer(many=False, read_only=True)
    size = SizeSerializer(many=False, read_only=True)

    class Meta:
        model = RealEstate
        fields = "__all__"

    def get_ad_images(self, obj):
        ad_images = AdPicture.objects.filter(ad__id=obj.pk)
        serializer = AdPictureSerializer(ad_images, many=True).data
        return serializer


class AdSerializer (serializers.ModelSerializer):
    brand = Brand(many=False, read_only=True)
    color = Colors(many=False, read_only=True)
    type = TypeSerializer(many=False, read_only=True)
    material = MaterialSerializer(many=False, read_only=True)
    model = ModelSerializer(many=False, read_only=True)
    top_style = TopStyleSerializer(many=False, read_only=True)
    condition = Condition(many=False, read_only=True)
    size = SizeSerializer(many=False, read_only=True)
    country = CountrySerializer(many=False, read_only=True)
    city = CitySerializer(many=False, read_only=True)
    currency = CurrencySerializer(many=False, read_only=True)
    payment_method = PaymentMethodSerializer(many=False, read_only=True)
    size = SizeSerializer(many=False, read_only=True)
    user = UserSerializer(many=False)
    ad_images = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Ad
        fields = "__all__"

    def get_ad_images(self, obj):
        ad_images = AdPicture.objects.filter(ad__id=obj.pk)
        serializer = AdPictureSerializer(ad_images, many=True).data
        return serializer


class AdPolymorphicSerializer(PolymorphicSerializer):

    model_serializer_mapping = {
        Ad: AdSerializer,
        Fashion: FashionSerializer,
        Education: EducationSerializer,
        MotorBikes: MotorBikesSerializer,
        Electronics: ElectronicsSerializer,
        Car: CarSerializer,
        RealEstate: RealStateSerializer,
        Computer: ComputerSerializer,
    }
