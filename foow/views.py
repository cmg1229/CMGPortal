from django.shortcuts import render
from django.http import HttpResponse
from foow.models import BlogPost

# Create your views here.
def index(request):
	return render(request, 'foow/index.html')

def blogpost(request, id):
	b = BlogPost.objects.get(post_id=id)
	return render(request, 'foow/detail.html', {'BlogPost':b})
