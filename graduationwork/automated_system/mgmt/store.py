from .. import models
from . import helpers
import datetime


def saveProductsCount(payload):
    storeElemId = payload['storeElem_id']
    productsCount = int(payload['productsCount'])
    storeElem = models.Store.objects.get(id=storeElemId)
    storeElem.product_count = productsCount
    storeElem.save()
    result = helpers.getEmptyResultObject()
    result['success'] = storeElem.toJSON()
    return result


def addProducts(payload):
    storeElemId = payload['storeElem_id']
    addCount = int(payload['addCount'])
    storeElem = models.Store.objects.get(id=storeElemId)
    newProductCount = storeElem.product_count + addCount
    result = helpers.getEmptyResultObject()
    if newProductCount > 0:
        storeElem.product_count += addCount
        storeElem.last_charge = datetime.datetime.now()
        storeElem.save()
        result['success'] = storeElem.toJSON()
    else:
        result['failure'] = '"количество забираемых элементов не может превышать количество элементов на складе"'
    return result
