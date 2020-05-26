from .. import models
from . import helpers
import datetime
from django.db.models import Q


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


def changeParam(payload):
    storeElemId = payload['storeElem_id']
    paramName = payload['paramName']
    paramValue = payload['paramValue']
    result = helpers.getEmptyResultObject()

    sectionWithNoProducts = False
    storeElem = ''
    try:
        storeElem = models.Store.objects.get(id=storeElemId)
    except models.Store.DoesNotExist:
        sectionWithNoProducts = True
    if sectionWithNoProducts:
        result['failure'] = '"сначала надо добавить продукты"'
        return result
    if paramName == 'section_name':
        hasDuplicates = True
        try:
            hasDuplicates = models.Store.objects.filter(
                ~Q(section_name=storeElem.section_name)).get(section_name=paramValue)
        except models.Store.DoesNotExist:
            hasDuplicates = False
        if hasDuplicates:
            result['failure'] = '"имя секции должно быть уникальным"'
            return result
        else:
            storeElems = models.Store.objects.filter(
                section_name=storeElem.section_name)
            for storeElemInQuery in storeElems:
                storeElemInQuery.section_name = paramValue
                storeElemInQuery.save()
    else:
        storeElem.__dict__[paramName] = paramValue
        storeElem.save()
    storeElem = models.Store.objects.get(id=storeElemId)
    result['success'] = storeElem.toJSON()
    result['success'] = result['success'][:-1] + \
        ', "paramName": "' + str(paramName) + '"}'
    return result


def removeShelf(payload):
    shelfElemId = payload['shelfElem_id']
    result = helpers.getEmptyResultObject()
    removedShelf = models.Store.objects.get(id=shelfElemId)
    result['success'] = removedShelf.toJSON()
    removedShelf.delete()
    return result


def removeSection(payload):
    shelfElemId = payload['shelfElem_id']
    result = helpers.getEmptyResultObject()

    storeElem = models.Store.objects.get(id=shelfElemId)
    storeElemJSON = storeElem.toJSON()
    storeElems = models.Store.objects.filter(
        section_name=storeElem.section_name)
    for storeElemInQuery in storeElems:
        storeElemInQuery.delete()
    result['success'] = storeElemJSON
    return result


def addSection(payload):
    lastStoreElem = models.Store.objects.order_by('id').last()
    result = helpers.getEmptyResultObject()
    sectionName = 'section_'
    try:
        while True:
            models.Store.objects.get(section_name=sectionName)
            sectionName += "1"
    except models.Store.DoesNotExist:
        pass
    result['success'] = lastStoreElem.toJSON()[:-1] + ', "newSectionName": "' + \
        sectionName + '"}'
    return result


def addShelf(payload):
    sectionId = payload['storeElem_id']
    sectionName = payload['sectionName']
    result = helpers.getEmptyResultObject()

    newStoreElem = models.Store.objects.create(
        product=models.Product.objects.all().first(),
        product_count=1,
        width=0.0,
        height=0.0,
        length=0.0,
        carrying_capacity=0.0,
        shelf_name='NewShelf',
        section_name=sectionName
    )
    result['success'] = newStoreElem.toJSON(
    )[:-1] + ', "sectionId": "' + sectionId + '", "productName": "' + newStoreElem.product.name + '"}'
    return result


def changeProduct(payload):
    storeElemId = payload['storeElem_id']
    productName = payload['productName']
    result = helpers.getEmptyResultObject()

    storeProduct = ""
    storeElem = models.Store.objects.get(id=storeElemId)
    print(productName)
    try:
        storeProduct = models.Product.objects.get(name=productName)
    except models.Product.DoesNotExist:
        result['failure'] = '"такого продукта не существует"'
        return result
    storeElem.product = storeProduct
    storeElem.save()
    result['success'] = storeElem.toJSON()[:-1] + ', "productName": "' + \
        storeElem.product.name + '"}'
    return result
