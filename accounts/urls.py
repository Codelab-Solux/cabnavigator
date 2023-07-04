from django.urls import path
from django.contrib.auth import views as auth_views
from .views import *

urlpatterns = [
    path('signup/', signupView, name='signup'),
    path('login/', loginView, name='login'),
    path('logout/', logoutUser, name='logout'),
    path('users/', users, name='users'),
    path('users/<str:pk>/', user_profile, name='user_profile'),
    path('create_user/', create_user, name='create_user'),
    path('delete_user/<str:pk>/', delete_user, name='delete_user'),
    path('password/', auth_views.PasswordChangeView.as_view()),
]
