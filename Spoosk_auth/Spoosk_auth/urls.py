"""
URL configuration for Spoosk_auth project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from accounts.views import signup, signup_endpoint, login_endpoint
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup', signup, name='signup'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('signup_endpoint', signup_endpoint, name='signup_endpoint'),
    path('login_endpoint', login_endpoint, name='login_endpoint'),
    # path('/', include('accounts.urls')),
]
