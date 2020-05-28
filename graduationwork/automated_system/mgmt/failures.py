from django.contrib.auth.models import User
from .. import models
from . import helpers, db_manager, analytics as analytics_manager
import json
from _datetime import timedelta
import datetime
import re
import math


def assignTask(payload):
    taskId = payload['task_id']
    assigneeId = payload['assignee_id']
    result = helpers.getEmptyResultObject()

    task = models.Failure.objects.get(id=taskId)
    if assigneeId:
        task.assignee = models.User.objects.get(id=assigneeId)
    else:
        task.assignee = None
    task.save()
    taskJSON = task.toJSON()[:-1]
    users = User.objects.all()
    resultJSON = taskJSON + ', ' + db_manager.getAllAvailableUsersJSON() + '}'
    result['success'] = resultJSON
    return result


def solveTask(payload):
    taskId = payload['task_id']
    result = helpers.getEmptyResultObject()

    task = models.Failure.objects.get(id=taskId)
    task.is_solved = True
    task.save()
    taskJSON = task.toJSON()[:-1]
    users = User.objects.all()
    resultJSON = taskJSON + ', ' + db_manager.getAllAvailableUsersJSON() + '}'
    result['success'] = resultJSON
    return result


def checkForFailures(shelfId):
    currentDateAndTime = datetime.datetime.now()
    shelfElem = models.Store.objects.get(id=shelfId)
    max_last_charge_interval = 1
    shelfStats = analytics_manager.getStatsForShelf(shelfElem)
    min_recommended = shelfStats[0]
    max_recommended = shelfStats[1]
    avg_recommended = shelfStats[2]
    shouldBeChecked = (shelfElem.last_charge +
                       timedelta(hours=max_last_charge_interval) < currentDateAndTime)

    shelfAlreadyInFailures = False
    for failure in models.Failure.objects.all():
        shelfAlreadyInFailures = bool(re.match(shelfElem.shelf_name, failure.text)) and bool(
            re.match(shelfElem.section_name, failure.text))
        if shelfAlreadyInFailures and not failure.is_solved:
            break
        else:
            shelfAlreadyInFailures = False

    if min_recommended > shelfElem.product_count and not shelfAlreadyInFailures:
        severity_denominator = min_recommended / 5
        severity = 0
        if shelfElem.product_count == 0:
            severity = 5
        else:
            severity = 5 - \
                math.floor(shelfElem.product_count / severity_denominator)
        models.Failure.objects.create(
            text="Shelf should be filled in by " +
            str(avg_recommended/2 - shelfElem.product_count) + " products. Shelf name: " + str(shelfElem.shelf_name) +
            ", section name: " + str(shelfElem.section_name) + ".",
            severity=severity,
            possible_cause="Customers bought a lot of products from that shelf.",
            possible_solution="Fill shelf in."
        )
    elif max_recommended < shelfElem.product_count and not shelfAlreadyInFailures:
        severity = max_recommended / \
            math.ceil(shelfElem.product_count - max_recommended)
        if severity > 5:
            severity = 5
        models.Failure.objects.create(
            text=str(shelfElem.product_count - max_recommended + avg_recommended/2) + " products should be transferred to the storage. Shelf name: " + str(shelfElem.shelf_name) +
            ", section name: " + str(shelfElem.section_name) + ".",
            severity=severity,
            possible_cause="Customers didn't buy a lot of products from that shelf.",
            possible_solution="Transfer products to the storage."
        )
    elif shouldBeChecked and not shelfAlreadyInFailures:
        models.Failure.objects.create(
            text="Number of products should be clarified. Shelf name: " + str(shelfElem.shelf_name) +
            ", section name: " + str(shelfElem.section_name) + ".",
            severity=2,
            possible_cause="A lot of time has passed since the last update.",
            possible_solution="Clarify the number of products."
        )

    if shelfAlreadyInFailures:
        for failure in models.Failure.objects.all():
            if bool(re.match(shelfElem.shelf_name, failure.text)) and bool(
                    re.match(shelfElem.section_name, failure.text)):
                if min_recommended < shelfElem.product_count and max_recommended > shelfElem.product_count and not shouldBeChecked:
                    failure.is_solved = True
                    failure.save()
