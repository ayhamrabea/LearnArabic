from django.urls import path
from . import views

urlpatterns = [
    path('singup',views.singup_page,name='singup'),
    path('login',views.login_page,name='login'),
    path('logout',views.logout_page,name='logout'),


]