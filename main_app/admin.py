from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Profile, City, Post

# Register your models here.

admin.site.register(Post)

admin.site.register(City)

admin.site.register(Profile)


