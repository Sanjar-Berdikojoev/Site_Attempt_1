from django.urls import path
from . import views

urlpatterns = [
    path('', views.mainpage_all, name='home'),
    path('instructor/create', views.InstructorCreateView.as_view(), name='instructor_create'),
    path('instructor/<int:id>/update', views.InstructorUpdateView.as_view(), name='instructor_update'),
    path('instructor/<int:id>/delete', views.InstructorDeleteView.as_view(), name='instructor_delete'),
    path('blog/create', views.BlogCreateView.as_view(), name='blog_create'),
    path('blog/<int:id>/update', views.BlogUpdateView.as_view(), name='blog_update'),
    path('blog/<int:id>/delete', views.BlogDeleteView.as_view(), name='blog_delete'),
    path('about_us/', views.about_us_view, name='about_us'),
    path('contacts/', views.contacts_view, name='contacts'),
    path('courses/', views.CoursesView.as_view(), name='courses'),
    path('courses/<int:id>/courses_info', views.course_detail, name='courses_info'),
    path('instructors/', views.instructor_view, name='instructors'),
    path('instructors/<int:id>/instructors_info', views.InstructorDetailView.as_view(), name='instructors_info'),
    path('blogs/', views.BlogsView.as_view(), name='blogs'),
    path('blogs/<int:id>/blogs_info', views.BlogsDetailView.as_view(), name='blogs_info'),
    path('traffic_laws/', views.traffic_rules_view, name='traffic_laws'),
    path('traffic_laws/<int:id>/traffic_laws_info', views.Traffic_RulesDetailView.as_view(), name='traffic_laws_info'),
    path('frequently_asked_questions/', views.FAQView.as_view(), name='frequently_asked_questions'),
    path('application_success/', views.application_success, name='application_success'),
]
