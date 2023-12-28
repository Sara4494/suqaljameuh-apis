
from modeltranslation.translator import translator, TranslationOptions
from varieties.models import *


class CategoryTranslationOptions(TranslationOptions):
    fields = ('name',)


class SubCategoryTranslationOptions(TranslationOptions):
    fields = ('name',)


class BrandTranslationOptions(TranslationOptions):
    fields = ('name',)


class MaterialTranslationOptions(TranslationOptions):
    fields = ('name',)


class TypeTranslationOptions(TranslationOptions):
    fields = ('name',)


class SubTypeTranslationOptions(TranslationOptions):
    fields = ('name',)


class TopStylelTranslationOptions(TranslationOptions):
    fields = ('name',)


class ConditionTranslationOptions(TranslationOptions):
    fields = ('name',)


class SizeTranslationOptions(TranslationOptions):
    fields = ('name',)


class ColorsTranslationOptions(TranslationOptions):
    fields = ('name',)


class QualificationTranslationOptions(TranslationOptions):
    fields = ('description',)


class EducationTranslationOptions(TranslationOptions):
    fields = ('description', )


class ExperienceTranslationOptions(TranslationOptions):
    fields = ('description',)


class PaymentMethodTranslationOptions(TranslationOptions):
    fields = ('name',)


class CurrencyTranslationOptions(TranslationOptions):
    fields = ('name',)


class CountryTranslationOptions(TranslationOptions):
    fields = ('name',)


class CityTranslationOptions(TranslationOptions):
    fields = ('name',)


class AmenityTranslationOptions(TranslationOptions):
    fields = ('name',)


class MechanismTranslationOptions(TranslationOptions):
    fields = ('name', )

 






class RentPeriodTranslationOptions(TranslationOptions):
    fields = ('name',)

class CapacityTranslationOptions(TranslationOptions):
    fields = ('name',)

class KiloMeterTranslationOptions(TranslationOptions):
    fields = ('name',)

class CreationYearTranslationOptions(TranslationOptions):
    fields = ('name',)

class OsTranslationOptions(TranslationOptions):
    fields = ('name',)

class MemoryTranslationOptions(TranslationOptions):
    fields = ('name',)

class ModelTranslationOptions(TranslationOptions):
    fields = ('name',)

class StorageranslationOptions(TranslationOptions):
    fields = ('name',)
 

class SiteTranslationOptions(TranslationOptions):
    fields = ('name',)

 

 
 
translator.register(Brand, BrandTranslationOptions)
translator.register(Material, MaterialTranslationOptions)
translator.register(Type, TypeTranslationOptions)
translator.register(SubType, SubTypeTranslationOptions)
translator.register(TopStyle, TopStylelTranslationOptions)
translator.register(Condition, ConditionTranslationOptions)
translator.register(Size, SizeTranslationOptions)
translator.register(Colors, ColorsTranslationOptions)
translator.register(Qualification, QualificationTranslationOptions)
translator.register(Education, EducationTranslationOptions)
translator.register(Experience, ExperienceTranslationOptions)
translator.register(PaymentMethod, PaymentMethodTranslationOptions)
translator.register(Currency, CurrencyTranslationOptions)
translator.register(Country, CountryTranslationOptions)
translator.register(City, CityTranslationOptions)
translator.register(Amenity, AmenityTranslationOptions)
translator.register(Mechanism, MechanismTranslationOptions)
 
translator.register(RentPeriod, RentPeriodTranslationOptions)
translator.register(Capacity, CapacityTranslationOptions)
translator.register(KiloMeter, KiloMeterTranslationOptions)
translator.register(OS, OsTranslationOptions)
translator.register(Memory, MemoryTranslationOptions)
translator.register(Model, ModelTranslationOptions)
translator.register(Storage, StorageranslationOptions)
translator.register(Site, SiteTranslationOptions)