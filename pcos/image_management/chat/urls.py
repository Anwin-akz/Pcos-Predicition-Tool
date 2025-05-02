from django.urls import path
from . import views

urlpatterns = [
    path('', views.chats, name='chats'),  # This serves the chats view at the root URL
    path('chats/', views.chats, name='chats'),
    path('chatbot_response/', views.chatbot_response, name='chatbot_response'),
]
