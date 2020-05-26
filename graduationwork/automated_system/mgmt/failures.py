from django.contrib.auth.models import User
from .. import models
from . import helpers, db_manager
import json


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
