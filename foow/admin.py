from django.contrib import admin
from .models import BlogPost, Album, Picture
# Register your models here.
admin.site.register(BlogPost)
admin.site.register(Album)
admin.site.register(Picture)
