from django.contrib import admin
from django.urls import path,include
from . import views


urlpatterns = [
    path('', views.chats, name='chats'),  # This serves the chats view at the root URL
    path('chats/', views.chats, name='chats'),
    path('chatbot_response/', views.chatbot_response, name='chatbot_response'),
    path('',views.predict_pcos, name='predict_pcos'),
    path('prediction/',views.predict_pcos, name='predict_pcos' ),
    path('image_upload/',views.image_pcos,name='image_pcos')
]
