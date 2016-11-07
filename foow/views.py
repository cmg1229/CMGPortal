import json
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.template import loader
from CMGPortal import settings
from foow.models import BlogPost

# Create your views here.
def index(request):
	b = BlogPost.objects.order_by('-pub_date')[:1]

	ascData = BlogPost.objects.order_by('post_id')
	asclist = [pst.post_id for pst in ascData]


	descData = BlogPost.objects.order_by('-post_id')
	desclist = [pst.post_id for pst in descData]


	template = loader.get_template('foow/index.html')
	context = {
		'posts' : b,
		'asclist' : asclist,
		'desclist' : desclist
	}
	return HttpResponse(template.render(context, request))

def blogdetail(request, id):
	b = BlogPost.objects.get(post_id=id)
	template = loader.get_template('foow/detail.html')
	context = {
		'post' : b
	}
	return HttpResponse(template.render(context, request))

def blogpost(request, id):
	b = BlogPost.objects.get(post_id=id)
	#return render(request, 'foow/detail.html', {'BlogPost':b})
	data = serializers.serialize('json', [b,])
	return HttpResponse(data,  content_type="application/json")

def allposts(request):
	b = BlogPost.objects.all()
	data = serializers.serialize('json', b)
	return HttpResponse(data, content_type="application/json")


def allidsdescending(request):
	data = BlogPost.objects.order_by('-pub_date')
	mylist = [{'post_id':pst.post_id} for pst in data]
	return HttpResponse(json.dumps(mylist), content_type="application/json")

def allidsascending(request):
	data = BlogPost.objects.order_by('pub_date')
	mylist = [{'post_id':pst.post_id} for pst in data]
	return HttpResponse(json.dumps(mylist), content_type="application/json")

@login_required
def add(request):
	if request.method == 'GET':
		return render(request, 'foow/addedit.html')
	if request.method == 'POST':
		title = request.POST['title']
		subtitle = request.POST['subtitle']
		blogcontent = request.POST['blogcontent']
		bp = BlogPost()
		bp.blog_title = title
		bp.blog_subtitle = subtitle
		bp.blog_text = blogcontent
		bp.save()
		return HttpResponseRedirect("/")

def Login(request):
	next = request.GET.get('next', '/addcmg/')
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)

		if user is not None:
			if user.is_active:
				login(request, user)
				return HttpResponseRedirect(next)
			else:
				return HttpResponse("Inactive User.")
		else:
			return HttpResponseRedirect(settings.LOGIN_URL)
	return render(request, "foow/login.html", {'redirect_to': next})

def Logout(request):
	logout(request)
	return HttpResponseRedirect(settings.LOGIN_URL)

