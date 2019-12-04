"""coursework URL Configuration

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


urlpatterns = [
    path('', views.index, name='home'),
    path('admin/', admin.site.urls),
    re_path(r'^about', TemplateView.as_view(template_name="about.html",
                                            extra_context={"header": "О сайте"})),
    re_path(r'^contact', TemplateView.as_view(template_name="contact.html")),
    # re_path(r'^system', views.system),
    # re_path(r'^system/messages', views.system_messages),
    # https://metanit.com/python/django/3.2.php - Определение маршрутов
    # https://metanit.com/python/django/3.3.php - Параметры представлений


    # Authorization
    path('accounts/', include('django.contrib.auth.urls')),
    # Registration
]
