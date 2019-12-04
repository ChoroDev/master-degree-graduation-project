from django.shortcuts import render
from django.http import HttpResponse
from .forms import UserForm


is_active = "class=is-active"


def index(request):
    if request.method == "POST":
        name = request.POST.get("name")
        # age = request.POST.get("age")     # получение значения поля age
        return HttpResponse("<h2>Hello, {0}</h2>".format(name))
    else:
        userform = UserForm()
        return render(request, "index.html", {"form": userform, "home_is_active": is_active})


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
