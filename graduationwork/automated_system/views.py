from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from .forms import UserForm
from .mgmt import db_manager
from . import models
import json
import math


is_active = "active"


def index(request):
    # currentStatus = db_manager.get_current_status()
    currentStatus = ""
    userform = UserForm()
    return render(request, "index.html", {"form": userform, "home_is_active": is_active, "current_status": currentStatus})


def store(request):
    if request.method == 'POST':
        print('custom post')
        # db_manager.update_store_products(request.POST.get(
        #     'product_id'), request.POST.get('storeProducts'))
        print(request.POST.get('storeProducts'))
        print(request.POST.get('storageProducts'))
        # db_manager.update_storage_products(request.POST.get(
        #     'product_id'), request.POST.get('storageProducts'))
        return HttpResponse('')
    else:
        # storageProducts = db_manager.get_storage_products()
        # storageProducts = serializers.serialize('json', storageProducts)
        storageProducts = ""
        # storeProducts = db_manager.get_store_products()
        # storeProducts = serializers.serialize('json', storeProducts)
        storeProducts = ""
        return render(request, "store.html", {"store_is_active": is_active, "storageProducts": storageProducts, "storeProducts": storeProducts})


def storage(request):
    # storageProducts = db_manager.get_storage_products_for_page()
    storageProducts = ""
    return render(request, "storage.html", {"storage_is_active": is_active, "products_in_storage": storageProducts})


def transportations(request):
    # transpos = db_manager.get_transportations_info()
    transpos = ""
    return render(request, "transportations.html", {"transportations_is_active": is_active, "transportations": transpos})


def about(request):
    return render(request, "about.html", {"about_is_active": is_active})


def contact(request):
    return render(request, "contact.html", {"contact_is_active": is_active})


def product(request):
    return render(request, "product.html")


def products(request):
    products = models.Product.objects.all()
    rowsCount = math.ceil(products.count() / 3)
    return render(
        request,
        "products.html",
        {
            "products_is_active": is_active,
            "products": models.Product.objects.all(),
            "rowsCount": rowsCount
        }
    )
