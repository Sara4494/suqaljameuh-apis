from modeltranslation.translator import translator, TranslationOptions
from memberships.models import *


class MembershipTranslationOptions(TranslationOptions):
    fields = ('name',)


class FeaturedMembershipTranslationOptions(TranslationOptions):
    fields = ('name',)


class AdMembershipTranslationOptions(TranslationOptions):
    fields = ('name',)


translator.register(Membership, MembershipTranslationOptions)
translator.register(FeaturedMembership, FeaturedMembershipTranslationOptions)
translator.register(AdMembership, AdMembershipTranslationOptions)
