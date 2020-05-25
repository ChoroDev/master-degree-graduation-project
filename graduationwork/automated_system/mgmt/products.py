from .. import models
from . import helpers
from django.db.models import Q
import re
import os


SITE_ROOT = os.path.dirname(os.path.realpath(__file__))
IMAGES_PATH = '\\..\\static\\images\\'


def handleChangeImage(request):
    image = request.FILES.get('img')
    productId = request.POST.get('product_id')
    imageName = models.Product.objects.get(
        id=productId).name + '.png'
    imagePath = SITE_ROOT + IMAGES_PATH + imageName
    saveImage(image, imagePath)
    successResponse = '{"success": {"id": "' + productId + \
        '", "name": "' + imageName + \
        '", "message": "картинка успешно сохранена"} }'
    return successResponse


def saveImage(image, path):
    with open(path, 'wb+') as destination:
        for chunk in image.chunks():
            destination.write(chunk)


def saveChanges(payload):
    productId = payload['product_id']
    newName = payload['name']
    newPrice = payload['price']
    newDigitCode = payload['digitCode']
    newShelfLife = payload['shelfLife']
    newWidth = payload['width']
    newHeight = payload['height']
    newLength = payload['length']
    newWeight = payload['weight']
    newStackable = payload['stackable']

    result = helpers.getEmptyResultObject()
    product = models.Product.objects.get(id=productId)
    oldImagePath = ""
    newImagePath = ""
    hasDuplicates = False

    try:
        hasDuplicates = models.Product.objects.filter(
            ~Q(id=productId)).get(name=newName)
    except models.Product.DoesNotExist:
        oldImageName = product.name
        oldImagePath = SITE_ROOT + IMAGES_PATH + oldImageName + '.png'
        newImagePath = SITE_ROOT + IMAGES_PATH + newName + '.png'
        hasDuplicates = False
    if hasDuplicates:
        result['failure'] = '"имя должно быть уникальным"'
        return result

    try:
        isFloat = float(newPrice)
    except ValueError:
        result['failure'] = '"цена должна быть целым или дробным числом"'
        return result

    isDigitCodeValid = bool(re.match("^[0-9]{5}-[0-9]{4}$", newDigitCode))
    if not isDigitCodeValid:
        result['failure'] = '"код должен состоять из цифр в формате XXXXX-XXXX"'
        return result
    else:
        try:
            hasDuplicates = models.Product.objects.filter(
                ~Q(id=productId)).get(digit_code=newDigitCode)
        except models.Product.DoesNotExist:
            hasDuplicates = False
        if hasDuplicates:
            result['failure'] = '"код должен быть уникальным"'
            return result

    try:
        isInt = float(newShelfLife)
    except ValueError:
        result['failure'] = '"срок годности должен быть целым числом"'
        return result

    try:
        isFloat = float(newWidth)
        isFloat = float(newHeight)
        isFloat = float(newLength)
        isFloat = float(newWeight)
    except ValueError:
        result['failure'] = '"физические параметры должны быть целыми или дробными числами"'
        return result

    isStackableValid = bool(re.match("^(Да|Нет)$", newStackable))
    if not isStackableValid:
        result['failure'] = '"складируемость должна быть \"Да\" или \"Нет\""'
        return result
    else:
        if bool(re.match("^Да$", newStackable)):
            newStackable = True
        else:
            newStackable = False

    product.name = newName
    product.price = newPrice
    product.digit_code = newDigitCode
    product.shelf_life = newShelfLife
    product.width = newWidth
    product.height = newHeight
    product.length = newLength
    product.weight = newWeight
    product.stackable = newStackable
    product.save()
    os.rename(oldImagePath, newImagePath)
    result['success'] = product.toJSON()
    return result


def removeProduct(payload):
    productId = payload['product_id']
    removedProduct = models.Product.objects.get(id=productId)
    removedProductJSON = removedProduct.toJSON()
    removedProduct.delete()
    result = helpers.getEmptyResultObject()
    result['success'] = removedProductJSON
    return result


def addProductCard(payload):
    result = helpers.getEmptyResultObject()
    productName = "product"
    try:
        while True:
            models.Product.objects.get(name=productName)
            productName += "1"
    except models.Product.DoesNotExist:
        pass

    lastDigitCode = models.Product.objects.order_by(
        'digit_code').last().digit_code
    firstNumber = int(lastDigitCode[:5])
    secondNumber = int(lastDigitCode[6:])
    if secondNumber + 1 > 9999:
        if firstNumber + 1 > 99999:
            result['failure'] = '"достигнут лимит номеров продуктов. обратитесь к системному администратору"'
        firstNumber += 1
        secondNumber = 0
    else:
        secondNumber += 1
    firstNumberStr = str(firstNumber)
    while len(firstNumberStr) < 5:
        firstNumberStr = "0" + firstNumberStr
    secondNumberStr = str(secondNumber)
    while len(secondNumberStr) < 4:
        secondNumberStr = "0" + secondNumberStr
    digitCode = firstNumberStr + "-" + secondNumberStr

    product = models.Product.objects.create(
        name=productName,
        digit_code=digitCode,
        shelf_life=1,
        width=0.0,
        height=0.0,
        length=0.0,
        weight=0.0,
        price=0.0,
        stackable=False)
    result['success'] = product.toJSON()
    return result
