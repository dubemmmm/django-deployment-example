from django.urls import path
from . import views
app_name = 'first_app1'

urlpatterns = [
    path('', views.index, name='index'),
    path('user_login', views.user_login, name='user_login'),
    path('register', views.register, name='register'),
    path('user_logout', views.user_logout, name='user_logout'),
    path('homepage', views.homepage, name='homepage'),
 
]
