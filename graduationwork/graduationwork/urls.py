"""graduationwork URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, re_path, include
from automated_system import views
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views
from django.contrib.auth.forms import AuthenticationForm

AuthenticationForm.login_is_active = "nav_item_active"

urlpatterns = [
    path('', views.index, name='home'),
    path('admin/', admin.site.urls),
    path('store', views.store, name='store'),
    path('storage', views.storage, name='storage'),
    path('transportations', views.transportations, name='transportations'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('login', auth_views.LoginView.as_view(
         template_name='auth/login.html', authentication_form=AuthenticationForm), name='login'),
    path('logout', auth_views.LogoutView.as_view(
        template_name='index.html'), name='logout'),
    path('products', views.products, name='products'),
]
