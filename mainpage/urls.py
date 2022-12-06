from django.urls import path
from . import views
urlpatterns = [
    path('', views.mainpage_all, name=''),
    path('<int:id>/', views.extended_info, name=''),
    # path('', views.courses, name=''),
    # path('', views.blogs, name=''),
    # path('', views.traffic_laws, name=''),
]
