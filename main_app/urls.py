from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('accounts/', include('django.contrib.auth.urls')),
    # path('accounts/signup', views.signup, name='signup'),
    path('profile/', views.profile, name='profile' ),
    path('post/create/', views.post_create, name='post_create'),
    path('post/<int:post_id>/edit', views.post_edit, name='post_edit')
    
]
