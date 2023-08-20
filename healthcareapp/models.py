from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from django.conf import settings
class CustomUser(AbstractUser):
    USER_TYPE_CHOICES = (
        ('patient', 'Patient'),
        ('doctor', 'Doctor'),
    )
    
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES, default='patient')
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    address_line1 = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    pincode = models.CharField(max_length=10)

    def __str__(self):
        return self.username
class Category(models.Model):
    name=models.CharField(max_length=30)
    def __str__(self) -> str:
        return self.name  
class BlogPost(models.Model):
    CONTENT_TYPE_CHOICES = (('upload','Upload'),
                          ('draft','Draft'),
    )
    title=models.CharField(max_length=100)
    Image=models.ImageField(upload_to='blog_image/')
    Category=models.ForeignKey(Category,on_delete=models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    Summary=models.CharField(max_length=300)
    content=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    draft=models.CharField(max_length=10,choices=CONTENT_TYPE_CHOICES,default='draft')
    def __str__(self):
        return self.title
