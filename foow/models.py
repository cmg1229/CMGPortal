from __future__ import unicode_literals
from django.conf import settings
from django.db import models
from django.utils import timezone
from django.core.files.storage import FileSystemStorage

# Create your models here.

fs = FileSystemStorage(location=settings.MEDIA_ROOT)

class BlogPost(models.Model):
    post_id = models.AutoField(primary_key=True)
    blog_title = models.CharField(max_length=70,null=True)
    blog_subtitle = models.CharField(max_length=70,null=True,blank=True)
    blog_text = models.CharField(max_length=10000,default="blog text")
    pub_date = models.DateTimeField(default=timezone.now)
    mod_date = models.DateTimeField(default=timezone.now)
    picture = models.FileField(storage=fs, null=True, blank=True)

    def __unicode__(self):
    	return self.blog_title + " " + self.blog_subtitle

    def __str__(self):
    	return self.blog_title + " " + self.blog_subtitle

    class Meta:
    	ordering = ["-pub_date"]