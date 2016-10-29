import json
from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from foow.models import BlogPost

# Create your views here.
def index(request):
	return render(request, 'foow/index.html')

def blogpost(request, id):
	b = BlogPost.objects.get(post_id=id)
	#return render(request, 'foow/detail.html', {'BlogPost':b})
	data = serializers.serialize('json', [b,])
	return HttpResponse(data,  content_type="application/json")

def allposts(request):
	b = BlogPost.objects.all()
	data = serializers.serialize('json', b)
	return HttpResponse(data, content_type="application/json")