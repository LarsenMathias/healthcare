from django.contrib import admin
from .models import CustomUser,BlogPost,Category
# Register your models here.
admin.site.register(CustomUser)
admin.site.register(BlogPost)
admin.site.register(Category)