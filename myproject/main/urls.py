from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('create/', views.create_plan, name='create'),
    path('plan/', views.plan, name='plan'),
    path('chat/', views.chat_page, name='chat'),
    path('api/chat/', views.chatbot),
]