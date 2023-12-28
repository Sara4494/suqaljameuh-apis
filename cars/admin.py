from django.contrib import admin
from cars.models import *
# Register your models here.
admin.site.register(FoulType)
admin.site.register(BodyType)
admin.site.register(InternalSpecs)
admin.site.register(RegionalSpecs)
admin.site.register(OuterSpecs)