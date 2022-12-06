from django.urls import path
from . import views
urlpatterns = [
    path('', views.mainpage_all, name='home'),
    path('<int:id>/', views.instructor_extended_info, name=''),
    path('<int:id>/', views.course_extended_info, name=''),
    path('<int:id>/', views.blogs_extended_info, name=''),
    path('<int:id>/', views.traffic_laws_extended_info, name=''),
]
