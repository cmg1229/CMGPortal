from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<id>[0-9]+)/$', views.blogpost, name='Blog Post'),
    url(r'^post/(?P<id>[0-9]+)/$', views.blogdetail, name='Blog Post'),
    url(r'^allposts/', views.allposts, name='All Posts'),
    url(r'^allidsdescending/', views.allidsdescending),
    url(r'^allidsascending/', views.allidsascending),
    url(r'^addcmg/', views.add, name='New Post'),
    url(r'^addalbum/', views.addalbum, name='New Album'),
    url(r'^addpicture/', views.addpicture, name='New Picture'),
    url(r'^login/', views.Login),
    url(r'^logout/', views.Logout),
    url(r'^contact/', views.contact),
    url(r'^gallery/', views.gallery, name="Photo Gallery"),
    url(r'^album/(?P<id>[0-9]+)/$', views.album),
    url(r'^picture/(?P<id>[0-9]+)/$', views.picture),

]
