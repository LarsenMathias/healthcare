from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('', views.signup, name='signup'),
    path('login/', views.user_login, name='login'),
      path('dashboard/', views.dashboard, name='dashboard'),
         path('logout/', views.logout, name='logout'),
         path('blogpost/',views.blogpost,name='blogpost'),
        path('blog_detail/<int:post_id>/', views.blog_detail, name='blog_detail'),
path('blogpost/<int:category_id>/', views.blogpost, name='blogpost_category'),
path('upload_blog',views.upload_blog,name='upload_blog')

  

    # Add other views if needed
]
