from django.contrib.auth.models import User
from . import helpers, db_manager
from .. import models
import json


def saveChanges(payload):
    profileId = payload['profile_id']
    firstName = payload['firstName']
    lastName = payload['lastName']
    email = payload['email']
    group = 'Персонал'
    result = helpers.getEmptyResultObject()

    try:
        group = payload['group']
    except KeyError:
        pass

    profile = models.User.objects.get(id=profileId)
    users = User.objects.all()
    foundUser = ''
    for user in users:
        if user.profile == profile:
            user.first_name = firstName
            user.last_name = lastName
            user.email = email
            foundUser = user
    if group == 'Персонал':
        profile.group = 'P'
    elif group == 'Менеджеры':
        profile.group = 'M'
    elif group == 'Системные администраторы':
        profile.group = 'A'
    else:
        result['failure'] = '"ошибочное название группы"'
        return result

    foundUser.save()
    profile.save()
    result['success'] = profile.toJSON()
    return result


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
