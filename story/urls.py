from django.urls import path 
from .import views
urlpatterns = [

    path('',views.index,name='story'),
    path('detail/<int:id>',views.show_story,name='show_story'),

] 