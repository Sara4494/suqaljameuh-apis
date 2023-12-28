from django.contrib import admin
from .models import *
# from modeltranslation.admin import TranslationAdmin

from .translation import *
admin.site.register(Material)
admin.site.register(Type)
admin.site.register(Size)
admin.site.register(TopStyle)
# admin.site.register(SubCategory)
admin.site.register(Qualification)
admin.site.register(Education)
admin.site.register(Experience)
admin.site.register(PaymentMethod)
admin.site.register(Currency)
admin.site.register(Country)
admin.site.register(Condition)
admin.site.register(City)
admin.site.register(Amenity)
admin.site.register(Colors)
admin.site.register(Brand)
