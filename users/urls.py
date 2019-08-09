"""Defines url patterns for users."""

from django.urls import path,re_path
from django.conf.urls import url
from django.contrib.auth.views import LoginView
from django.urls import include
from . import views

urlpatterns = [

    re_path(r'^login/$', views.login, name='login'),

    re_path(r'^logout/$', views.logout_view, name='logout'),

    re_path(r'^register/$', views.register, name='register'),
 
    path(r'^captcha/', include(('captcha.urls','captcha'),namespace='captcha')),
    
    path(r'captcha/',include('captcha.urls')),
]
