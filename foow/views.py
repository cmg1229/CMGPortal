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
from foow.models import BlogPost, HitCount, Album, Picture

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

def gallery(request):
	albums = Album.objects.order_by('-album_created')
	template = loader.get_template('foow/gallery.html')
	context = {
		'albums' : albums
	}
	return HttpResponse(template.render(context, request))

def album(request, id):
	album = Album.objects.get(album_id = id)
	template = loader.get_template('foow/album.html')
	pictures = album.picture_set.all()
	context = {
		'album' : album,
		'pictures' : pictures
	}
	return HttpResponse(template.render(context, request))
	
def picture(request, id):
	picture = Picture.objects.get(picture_id = id)
	data = serializers.serialize('json', [picture,])
	return HttpResponse(data, content_type="application/json")

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

@login_required
def addalbum(request):
	if request.method == 'GET':
		return render(request, 'foow/addalbum.html')
	if request.method == 'POST':
		title = request.POST['title']
		album = Album()
		album.album_name = request.POST['title']
		album.save()
		return HttpResponseRedirect("/")

@login_required
def addpicture(request):
	if request.method == 'GET':
		template = loader.get_template('foow/addpicture.html')
		albums = Album.objects.order_by('-album_created')
		context = {
			"albums" : albums
		}
		return HttpResponse(template.render(context, request))
	if request.method == 'POST':
		pic = Picture()
		pic.album = Album.objects.get(album_id = int(request.POST['selectedalbumid']))
		pic.picture_description = request.POST["imagedescription"]
		pic.picture = request.FILES['imageprimary'] if 'imageprimary' in request.FILES else false
		pic.thumbnail = request.FILES['imagethumb'] if 'imagethumb' in request.FILES else false
		if request.POST.get('albumCover', False):
			pic.album_header = True
		else:
			pic.album_header = False
		pic.save()
		return HttpResponseRedirect("/album/"+request.POST['selectedalbumid'])


@login_required
def addpictures(request, id):
	album = Album.objects.get(album_id = id)
	template = loader.get_template('foow/addpictures.html')
	context = {
		"album" : album
	}
	if request.method == 'POST':
		pic = Picture()
		pic.album = album
		pic.picture = request.FILES["file"]
		pic.album_header = False
		pic.save()
	return HttpResponse(template.render(context, request))


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
		s.sendmail(email, [settings.ADMIN_EMAIL], msg.as_string())
		return HttpResponseRedirect("/")

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

