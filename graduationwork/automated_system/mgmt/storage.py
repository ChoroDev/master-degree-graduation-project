from .. import models
from . import helpers
import datetime


def addProducts(payload):
    storageElemId = payload['storageElem_id']
    addCount = int(payload['addCount'])
    storageElem = models.Storage.objects.get(id=storageElemId)
    newProductCount = storageElem.product_count + addCount
    result = helpers.getEmptyResultObject()
    if newProductCount > 0:
        storageElem.product_count += addCount
        storageElem.delivery_timestamp = datetime.datetime.now()
        storageElem.save()
        result['success'] = storageElem.toJSON()
    else:
        result['failure'] = '"количество забираемых элементов не может превышать количество элементов на складе"'
    return result


def saveProductsCount(payload):
    storageElemId = payload['storageElem_id']
    productsCount = int(payload['productsCount'])
    storageElem = models.Storage.objects.get(id=storageElemId)
    storageElem.product_count = productsCount
    storageElem.save()
    result = helpers.getEmptyResultObject()
    result['success'] = storageElem.toJSON()
    return result
