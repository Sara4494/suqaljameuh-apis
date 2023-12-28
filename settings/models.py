from django.db import models
from ckeditor.fields import RichTextField


class Page (models.Model) : 
    name = models.CharField(max_length=100)
    slug = models.SlugField(null=True)
    content = RichTextField()
    published_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'{self.name}'
    


class Settings(models.Model) : 
    website_name_ar = models.CharField(max_length=100,null=True)
    website_name_en = models.CharField(max_length=100, null=True)
    website_description_ar = models.CharField(max_length=100,null=True)
    website_description_en = models.CharField(max_length=100,null=True)
    keywords_ar = models.CharField(max_length=100,null=True)
    keywords_en = models.CharField(max_length=100,null=True)
    logo = models.ImageField(null=True,upload_to='settings-logo/')

    def __str__(self) : 
        return f'{self.website_name_en}'

 