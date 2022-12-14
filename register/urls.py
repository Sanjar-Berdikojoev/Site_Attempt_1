from django.urls import path
from . import views

app_name = 'users'


urlpatterns = [
    path('login/', views.NewLoginForm.as_view(), name='login'),
    path('registration/', views.Registration.as_view(), name='registration'),
    path('logout/', views.logout_user, name='logout'),
    path('sign-in/', views.sign_in, name='sign-in'),
]
