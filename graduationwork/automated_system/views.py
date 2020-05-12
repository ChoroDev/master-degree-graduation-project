from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from .forms import UserForm
from .mgmt import db_manager
from . import models
from collections import defaultdict
import json
import math


is_active = "active"


def index(request):
    # currentStatus = db_manager.get_current_status()
    currentStatus = ""
    userform = UserForm()
    return render(request, "index.html", {"form": userform, "home_is_active": is_active, "current_status": currentStatus})


def store(request):
    # if request.method == 'POST':
    #     print('custom post')
    #     db_manager.update_store_products(request.POST.get(
    #         'product_id'), request.POST.get('storeProducts'))
    #     print(request.POST.get('storeProducts'))
    #     print(request.POST.get('storageProducts'))
    #     db_manager.update_storage_products(request.POST.get(
    #         'product_id'), request.POST.get('storageProducts'))
    #     return HttpResponse('')
    # else:
    #     storageProducts = db_manager.get_storage_products()
    #     storageProducts = serializers.serialize('json', storageProducts)
    #     storageProducts = ""
    #     storeProducts = db_manager.get_store_products()
    #     storeProducts = serializers.serialize('json', storeProducts)
    #     storeProducts = ""
    #     return render(request, "store.html", {"store_is_active": is_active, "storageProducts": storageProducts, "storeProducts": storeProducts})

    storeSectionsRaw = defaultdict(list)
    for shelf in models.Store.objects.all():
        storeSectionsRaw[shelf.section_name].append(shelf)
    sectionsNames = storeSectionsRaw.keys()
    storeSections = storeSectionsRaw.values()
    return render(request, "store.html", {"store_is_active": is_active, "storeSections": storeSections, "sectionsNames": sectionsNames})


def storage(request):
    return render(request, "storage.html", {"storage_is_active": is_active, "storage": models.Storage.objects.all()})


def transportations(request):
    # transpos = db_manager.get_transportations_info()
    transpos = ""
    return render(request, "transportations.html", {"transportations_is_active": is_active, "transportations": transpos})


def about(request):
    return render(request, "about.html", {"about_is_active": is_active})


def contact(request):
    return render(request, "contact.html", {"contact_is_active": is_active})


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


def profile(request):
    userGroups = list()
    for group in request.user.groups.all():
        userGroups.append(group.name)
    userGroup = "Персонал"

    tasksByUsersDict = defaultdict(list)
    unassignedTasks = list()
    for task in models.Failure.objects.all():
        if task.assignee:
            tasksByUsersDict[task.assignee.id].append(task)
        else:
            unassignedTasks.append(task)
    tasks = tasksByUsersDict

    shelvesByUsersDict = defaultdict(list)
    unassignedShelves = list()
    for shelf in models.Store.objects.all():
        if shelf.user:
            shelvesByUsersDict[shelf.user.id].append(shelf)
        else:
            unassignedShelves.append(shelf)
    shelves = shelvesByUsersDict

    if userGroups:
        if userGroups[0] == "SystemAdministrators":
            userGroup = "Системные администраторы"
        elif userGroups[0] == "Management":
            userGroup = "Менеджеры"
        else:
            userGroup = "Персонал"

    return render(
        request,
        "profile.html",
        {
            "profile_is_active": is_active,
            "userGroup": userGroup,
            "tasks": tasks,
            "unassignedTasks": unassignedTasks,
            "shelves": shelves,
            "unassignedShelves": unassignedShelves,
            "availableUsers": models.User.objects.all()
        }
    )
