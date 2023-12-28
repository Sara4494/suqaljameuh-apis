from django.contrib import admin
from memberships.models import FeaturedMember, FeaturedMembership, Membership, UserMembership, AdMembership
# Register your models here.
from .translation import *
admin.site.register(FeaturedMember)
admin.site.register(FeaturedMembership)
admin.site.register(Membership)
admin.site.register(UserMembership)
admin.site.register(AdMembership)
