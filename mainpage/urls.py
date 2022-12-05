from django.urls import path
from . import views
urlpatterns = [
    path('', views.mainpage_all, name=''),
    path('1', views.courses, name='1'),
    path('2', views.blogs, name='2'),
    path('3', views.traffic_laws, name='3'),
]
