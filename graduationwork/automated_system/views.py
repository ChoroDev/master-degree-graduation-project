from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from django.db.models import Count
from .forms import UserForm
from .mgmt import db_manager
from . import models
from collections import defaultdict
from qsstats import QuerySetStats
from django.utils import timezone
import json
import math
import datetime
import pytz


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
    userGroups = list()
    for group in request.user.groups.all():
        userGroups.append(group.name)
    userGroup = "Персонал"
    if userGroups:
        if userGroups[0] == "SystemAdministrators":
            userGroup = "Системные администраторы"
        elif userGroups[0] == "Management":
            userGroup = "Менеджеры"
        else:
            userGroup = "Персонал"

    storeSectionsRaw = defaultdict(list)
    for shelf in models.Store.objects.all():
        if userGroup == "Персонал":
            if shelf.user == request.user.profile:
                storeSectionsRaw[shelf.section_name].append(shelf)
        else:
            storeSectionsRaw[shelf.section_name].append(shelf)
    sectionsNames = storeSectionsRaw.keys()
    storeSections = storeSectionsRaw.values()
    return render(request, "store.html", {"store_is_active": is_active, "storeSections": storeSections, "sectionsNames": sectionsNames})


def storage(request):
    return render(request, "storage.html", {"storage_is_active": is_active, "storage": models.Storage.objects.all()})


def about(request):
    return render(request, "about.html", {"about_is_active": is_active})


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
    if userGroups:
        if userGroups[0] == "SystemAdministrators":
            userGroup = "Системные администраторы"
        elif userGroups[0] == "Management":
            userGroup = "Менеджеры"
        else:
            userGroup = "Персонал"

    tasksByUsersDict = defaultdict(list)
    unassignedTasks = list()
    for task in models.Failure.objects.all():
        if not task.is_solved:
            if request.user.profile.group == "P":
                if task.assignee == request.user.profile:
                    tasksByUsersDict[request.user.profile.id].append(task)
            else:
                if task.assignee:
                    tasksByUsersDict[task.assignee.id].append(task)
                else:
                    unassignedTasks.append(task)
    tasks = tasksByUsersDict.values()

    shelvesByUsersDict = defaultdict(list)
    unassignedShelves = list()
    for shelf in models.Store.objects.all():
        if request.user.profile.group == "P":
            if shelf.user == request.user.profile:
                shelvesByUsersDict[request.user.profile.id].append(shelf)
        else:
            if shelf.user:
                shelvesByUsersDict[shelf.user.id].append(shelf)
            else:
                unassignedShelves.append(shelf)
    shelves = shelvesByUsersDict.values()

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
            "availableUsers": models.BaseUser.objects.all().select_related('profile')
        }
    )


def failures(request):
    solvedTasks = list()
    unsolvedTasks = list()
    for task in models.Failure.objects.all():
        if request.user.profile.group == "P":
            if task.assignee == request.user.profile:
                if not task.is_solved:
                    unsolvedTasks.append(task)
                else:
                    solvedTasks.append(task)
        else:
            if not task.is_solved:
                unsolvedTasks.append(task)
            else:
                solvedTasks.append(task)

    return render(
        request,
        "failures.html",
        {
            "failures_is_active": is_active,
            "solvedTasks": solvedTasks,
            "unsolvedTasks": unsolvedTasks,
            "availableUsers": models.BaseUser.objects.all().select_related('profile')
        }
    )


def analytics(request):
    start_date = datetime.date.today() - datetime.timedelta(days=10)
    end_date = datetime.date.today()
    stats = models.Statistics.objects.all()

    stats = models.Statistics.objects.all()
    firstShelfStore = models.Store.objects.get(id=1)
    firstShelfStats = list()
    for shelfStats in stats:
        if shelfStats.shelf == firstShelfStore:
            firstShelfStats.append(
                [f"Day: {shelfStats.id}", shelfStats.sold_count])

    values = firstShelfStats
    summary = [["khe", 100], ["kok", 120], ["hah", 230]]
    return render(request, "analytics.html", {"analytics_is_active": is_active, "values": values, "summary": summary})
