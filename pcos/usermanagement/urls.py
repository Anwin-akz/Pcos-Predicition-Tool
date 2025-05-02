from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path ('',views.index),
    # path ('',views.home),
    path ('about',views.about),
    path ('register',views.register),
    path ('login',views.sigin),
    path ('user',views.user),
    path ('logout',views.do_logout),
    path ('view_user',views.view_user),
    path ('feed_back',views.feed_back),
    path ('view_feedback',views.view_feedback),
    path ('image_upload',views.image_upload),
    path ('Resources',views.Resources),
    path ('chat',views.chat)
    

    
]
