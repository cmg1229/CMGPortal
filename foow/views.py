import json
import smtplib
from email.mime.text import MIMEText
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.template import loader
from CMGPortal import settings
from foow.models import BlogPost, HitCount

# Create your views here.
def index(request):
	b = BlogPost.objects.order_by('-pub_date')

	ascData = BlogPost.objects.order_by('post_id')
	asclist = [pst.post_id for pst in ascData]


	descData = BlogPost.objects.order_by('-post_id')
	desclist = [pst.post_id for pst in descData]

	clientIP = get_client_ip(request)
	hit = HitCount()
	hit.client_ip = clientIP
	hit.save()

	template = loader.get_template('foow/index.html')
	context = {
		'posts' : b,
		'asclist' : asclist,
		'desclist' : desclist
	}
	return HttpResponse(template.render(context, request))

def blogdetail(request, id):
	b = BlogPost.objects.get(post_id=id)

	next = None
	prev = None
	nextpost = BlogPost.objects.filter(post_id__gt=id).order_by('post_id')[:1]
	if nextpost.exists():
		next = nextpost[0]
	prevpost = BlogPost.objects.filter(post_id__lt=id).order_by('-post_id')[:1]
	if prevpost.exists():
		prev = prevpost[0]
	template = loader.get_template('foow/detail.html')
	context = {
		'post' : b,
		'next' : next,
		'previous' : prev
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
		bp.picture = request.FILES['blogimage'] if 'blogimage' in request.FILES else false
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

def contact(request):
	if request.method =='GET':
		return render(request, 'foow/contact.html')
	if request.method == "POST":
		text = request.POST['message']
		email = request.POST['email']
		msg = MIMEText(text, 'plain')
		msg['Subject'] = 'Message From FOW blog'
		msg['To'] = settings.ADMIN_EMAIL
		msg['From'] = email
		s = smtplib.SMTP(settings.SMTP_ADDRESS)
		s.sendmail(email, settings.ADMIN_EMAIL, msg)
		return HttpResponseRedirect("/")

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

