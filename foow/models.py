from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

# Create your models here.

def defaultTitle():
	return {"blog_title", "Post Title"}

def defaultText():
    return {"blog_text", "Blog Text"}

class BlogPost(models.Model):
    post_id = models.AutoField(primary_key=True)
    blog_title = models.CharField(max_length=30,default='Default Title')
    blog_subtitle = models.CharField(max_length=30, default='Default SubTitle')
    blog_text = models.CharField(max_length=8000,default='Default Text')
    pub_date = models.DateTimeField(default=timezone.now())
    picture_location = models.CharField(max_length=50, null=True)
