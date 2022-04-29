"""ebidya URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from unicodedata import name
from django.contrib import admin
from django.urls import path, include
from . import views

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('account/', include('account.urls'), name='account'),
    path('course/', include('course.urls'), name='course'),
    path('pro/', include('premium.urls'), name='premium'),
    path('cart/', views.cart, name='cart'),
    path('register/', views.register, name='register'),
    path('panel/', include('panel.urls'), name='panel'),
    path('search/', views.search, name='search'),
    path('watch/<str:exam_name>/<str:video_id>', views.watch, name='watch'),
    path('like_video/', views.like_video, name='like_video'),
    path('comment_video/', views.comment_video, name='comment_video'),
    path('loadComments/', views.loadComments, name='loadComments'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)