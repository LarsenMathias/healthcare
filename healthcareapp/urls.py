from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.user_login, name='login'),
      path('dashboard/', views.dashboard, name='dashboard'),
         path('logout/', views.logout, name='logout'),
    # Add other views if needed
]
