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
    blog_title = models.CharField(max_length=30,null=True)
    blog_subtitle = models.CharField(max_length=30,null=True)
    blog_text = models.CharField(max_length=8000,default="blog text")
    pub_date = models.DateTimeField(null=True)
    picture_location = models.CharField(max_length=30,null=True)
