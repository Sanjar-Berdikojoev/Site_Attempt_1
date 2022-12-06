from django.urls import path
from . import views

app_name = 'users'
urlpatterns = [
    path('registration/', views.Registration.as_view(), name='registration'),
    path('login/', views.NewLoginForm.as_view(), name='login'),
    path('users/', views.UserListView.as_view(), name='user_list'),
    path('logout/', views.logout_user, name='logout'),
    path('sign-in/', views.sign_in, name='sign-in'),
]
