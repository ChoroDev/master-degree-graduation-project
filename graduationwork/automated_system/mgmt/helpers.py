from django.http import HttpResponse
import json


def handleAction(request, manager):
    action = getattr(manager, request.POST.get('action'))
    payload = json.loads(request.POST.get('payload'))
    result = action(payload)
    if result['success']:
        successResponse = '{"success": ' + result['success'] + '}'
        return HttpResponse(successResponse)
    else:
        failureResponse = '{"failure": ' + result['failure'] + '}'
        return HttpResponse(failureResponse)


def getEmptyResultObject():
    return {'success': '', 'failure': ''}
