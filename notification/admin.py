from django.contrib import admin
from .models import Notification
from varieties.models import SubCategory
from varieties.models import Category
from modeltranslation.translator import translator
from varieties.translation import *
from .models import NotificationSettings
admin.site.register([Notification ,Category, SubCategory, NotificationSettings])

admin.site.site_header = 'Suq Aljomaa'
admin.site.site_title = 'Suq Aljomaa Admin site'

 

translator.register(Category, CategoryTranslationOptions)
translator.register(SubCategory, SubCategoryTranslationOptions)
from modeltranslation.translator import translator, TranslationOptions
 
 
class NotificationTranslationOptions(TranslationOptions):
    fields = ('to_user','content','sent_at','read')
translator.register(Notification, NotificationTranslationOptions)