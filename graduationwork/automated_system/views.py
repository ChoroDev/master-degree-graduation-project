from django.shortcuts import render
from django.http import HttpResponse
from .mgmt import db_manager, helpers, storage as storage_manager, products as products_manager, analytics as analytics_manager
from .mgmt import failures as failures_manager, store as store_manager, profile as profile_manager
from . import models, forms
from collections import defaultdict
import json
import os.path
import math


is_active = "active"


def index(request):
    return render(request, "index.html", {"home_is_active": is_active})


def store(request):
    if request.method == 'POST':
        return helpers.handleAction(request, store_manager)
    else:
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
    if request.method == 'POST':
        return helpers.handleAction(request, storage_manager)
    else:
        return render(request, "storage.html", {"storage_is_active": is_active, "storage": models.Storage.objects.all()})


def about(request):
    return render(request, "about.html", {"about_is_active": is_active})


def products(request):
    if request.method == 'POST':
        if request.FILES.get('img', False):
            return HttpResponse(products_manager.handleChangeImage(request))
        else:
            return helpers.handleAction(request, products_manager)
    else:
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
    if request.method == 'POST':
        return helpers.handleAction(request, profile_manager)
    else:
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
    if request.method == 'POST':
        return helpers.handleAction(request, failures_manager)
    else:
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
    # Logic structure
    # fullStatsForEachShelf = [
    #   [
    #       storeShelf,
    #       {
    #           'soldEveryDay', soldInYear = [
    #               {'2018', soldInYear['2018'] = [[date, sold_count], [date, sold_count], ...]},
    #               {'2019', soldInYear['2019'] = [...]},
    #               {'2020', soldInYear['2020'] = [...]}
    #           ],
    #           'incomeEveryDay', incomeInYear = [
    #               {'2018', incomeInYear['2018'] = [[date, sold_count * price_that_day], [date, sold_count * price_that_day], ...]},
    #               {'2019', incomeInYear['2019'] = [...]},
    #               {'2020', incomeInYear['2020'] = [...]}
    #           ],
    #           'failuresCountByYear', failuresInYear = [
    #               {'2018', failuresInYear['2018'] = sum(failures_count)},
    #               {'2019', failuresInYear['2019'] = sum(...)},
    #               {'2020', failuresInYear['2020'] = sum(...)}
    #           ]
    #       }
    #   ], [storeShelf, {...}], ...
    # ]

    # models.Stock.objects.all().delete()
    # models.Statistics.objects.all().delete()
    # db_manager.fill_in_stocks()
    # db_manager.fill_in_statistics()

    if request.method == 'POST':
        return helpers.handleAction(request, analytics_manager)
    else:
        fullStatsForEachShelf = analytics_manager.getFullStats()
        return render(
            request,
            "analytics.html",
            {
                "analytics_is_active": is_active,
                "fullStatsForEachShelf": fullStatsForEachShelf
            }
        )
