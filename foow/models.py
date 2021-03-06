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

class HitCount(models.Model):
    hit_id = models.AutoField(primary_key=True)
    client_ip = models.CharField(max_length=72, null=False)
    hit_date = models.DateTimeField(default=timezone.now)

class Album(models.Model):
    album_id = models.AutoField(primary_key=True)
    album_name = models.CharField(max_length=72, null=False)
    album_created = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.album_name
    def album_header(self):
        return self.picture_set.filter(album_header = True)
    class Meta:
        ordering = ["-album_created"]

class Picture(models.Model):
    picture_id = models.AutoField(primary_key=True)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    picture_description = models.CharField(max_length=500, null=True) 
    picture = models.FileField(storage=fs, null=False, blank=False)
    thumbnail = models.FileField(storage=fs, null=True, blank=True) 
    album_header = models.BooleanField(default=False, null=False)
    def __str__(self):
        return self.album.album_name + ' '+ str(self.picture_id)
