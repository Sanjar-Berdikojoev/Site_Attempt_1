from django.urls import path
from . import views
urlpatterns = [
    path('', views.mainpage_all, name='home'),
    path('<int:id>/instructor', views.instructor_extended_info, name='instructor'),
    path('<int:id>/course', views.course_extended_info, name='course'),
    path('<int:id>/blog', views.blogs_extended_info, name='blog'),
    path('<int:id>/traffic_law', views.traffic_laws_extended_info, name='traffic_law'),
    path('instructor/create', views.InstructorCreateView.as_view(), name='instructor_create'),
    path('instructor/<int:id>/update', views.InstructorUpdateView.as_view(), name='instructor_update'),
    path('instructor/<int:id>/delete', views.InstructorDeleteView.as_view(), name='instructor_delete'),
]
