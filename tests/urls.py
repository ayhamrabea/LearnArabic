from django.urls import path 
from . import views
urlpatterns = [

    path('',views.home , name='quizes'),
    path('detail/<int:id>',views.detail_page,name='detail_quiz'),
    path('detail/api/get-quiz/<int:id>',views.get_quize,name='get-quize'),

] 