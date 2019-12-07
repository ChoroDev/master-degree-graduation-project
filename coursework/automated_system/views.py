from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserForm
from .mgmt import db_manager


is_active = "class=is-active"


def index(request):
    currentStatus = db_manager.get_current_status()
    userform = UserForm()
    return render(request, "index.html", {"form": userform, "home_is_active": is_active, "current_status": currentStatus})


def store(request):
    return render(request, "store.html", {"store_is_active": is_active})


def storage(request):
    return render(request, "storage.html", {"storage_is_active": is_active})


def transportations(request):
    return render(request, "transportations.html", {"transportations_is_active": is_active})


def about(request):
    return render(request, "about.html", {"about_is_active": is_active})


def contact(request):
    return render(request, "contact.html", {"contact_is_active": is_active})
