from .. import models
from . import helpers
import datetime
import math
from _datetime import timedelta


def getFullStats():
    storeShelves = models.Store.objects.all()
    fullStatsRaw = models.Statistics.objects.order_by('day')

    years = list(
        map(
            lambda singleYearRaw: singleYearRaw.strftime('%Y'),
            models.Statistics.objects.all().dates('day', 'year')
        )
    )

    fullStatsForEachShelf = []
    for storeShelf in storeShelves:
        soldInYear = {}
        incomeInYear = {}
        failuresInYear = {}
        for year in years:
            soldInYear[year] = []
            incomeInYear[year] = []
            failuresInYear[year] = 0

        for dailyStats in fullStatsRaw:
            if storeShelf == dailyStats.shelf:
                year = dailyStats.statYear
                soldInYear[year].append(
                    [dailyStats.day.strftime(
                        '%m/%d'), dailyStats.sold_count]
                )
                if dailyStats.stock:
                    incomeInYear[year].append(
                        [dailyStats.day.strftime(
                            '%m/%d'), dailyStats.sold_count * dailyStats.stock.stock_price]
                    )
                else:
                    incomeInYear[year].append(
                        [dailyStats.day.strftime(
                            '%m/%d'), dailyStats.sold_count * dailyStats.price_that_day]
                    )
                failuresInYear[year] += dailyStats.failures_count
        availableStats = {}
        if soldInYear:
            availableStats["soldEveryDay"] = soldInYear
        if incomeInYear:
            availableStats["incomeEveryDay"] = incomeInYear
        if failuresInYear:
            availableStats["failuresInYear"] = failuresInYear
        fullStatsForEachShelf.append(
            [storeShelf, availableStats]
        )
    return fullStatsForEachShelf


def handleNewData(payload):
    storeElemId = payload['storeElem_id']
    result = helpers.getEmptyResultObject()

    storeElem = models.Store.objects.get(id=storeElemId)

    day = payload['day']
    try:
        day = datetime.datetime.strptime(day, "%Y/%m/%d")
    except ValueError:
        day = None
        result['failure'] = '"неправильный формат даты"'
        return result

    sold_count = payload['sold_count']
    try:
        sold_count = int(sold_count)
    except ValueError:
        sold_count = None
        result['failure'] = '"количество проданных продуктов должно быть целым числом"'
        return result

    stock_id = payload['stock_id']
    stock = None
    if stock_id != '':
        try:
            stock = models.Stock.objects.get(id=stock_id)
        except models.Stock.DoesNotExist:
            result['failure'] = '"акция не найдена"'
            return result

    failures_count = payload['failures_count']
    try:
        failures_count = int(failures_count)
    except ValueError:
        result['failure'] = '"количество ошибок должно быть целым числом"'
        return result

    price_that_day = payload['price_that_day']
    try:
        price_that_day = float(price_that_day)
    except ValueError:
        result['failure'] = '"цена в указанный день должна быть целым или дробным числом"'
        return result

    statsElem = models.Statistics.objects.create(
        day=day,
        shelf=storeElem,
        sold_count=sold_count,
        stock=stock,
        failures_count=failures_count,
        price_that_day=price_that_day
    )
    result['success'] = statsElem.toJSON()
    return result


def calculateLastYearStats(currentDate, shelf, min_products_count, max_products_count, years_to_count, days_ago):
    stats_count = 0
    min_that_year = 0
    max_that_year = 0
    days_count = 10
    for i in range(1, days_count + 1):
        day = currentDate - timedelta(days=days_ago+i)
        try:
            stat = models.Statistics.objects.get(shelf=shelf, day=day)
            stats_count += 1
            if max_that_year < stat.sold_count:
                max_that_year = stat.sold_count
            if min_that_year > stat.sold_count:
                min_that_year = stat.sold_count
        except models.Statistics.DoesNotExist:
            pass

    if min_that_year < min_products_count:
        min_that_year = min_products_count
    if max_that_year > max_products_count:
        max_that_year = max_products_count

    if stats_count != 0:
        years_to_count += 1

    return [min_that_year, max_that_year, years_to_count]


def getStatsForShelf(shelf):
    currentDate = datetime.date.today()
    # 1. Essential borders

    min_products_count = math.floor(shelf.width / shelf.product.width)
    while min_products_count * shelf.product.weight >= 0.75 * shelf.carrying_capacity:
        min_products_count -= 1
    max_products_count = 0
    product_S = shelf.product.width * shelf.product.length
    product_V = product_S * shelf.product.height
    shelf_S = shelf.width * shelf.length
    shelf_V = shelf_S * shelf.height
    if shelf.product.stackable:
        max_products_count = math.floor(shelf_V / product_V)
    else:
        max_products_count = math.floor(shelf_S / product_S)
    while max_products_count * shelf.product.weight >= 0.75 * shelf.carrying_capacity:
        max_products_count -= 1
    if min_products_count > max_products_count:
        min_products_count = max_products_count

    products_count_average = (max_products_count + min_products_count) / 2

    years_to_count = 1

    # 2. Last few days borders

    relevance = 0.5
    stats_count = 0
    min_for_day_sum = 0
    max_for_day_sum = 0
    days_count = 10
    for i in range(1, days_count + 1):
        day = currentDate - timedelta(days=i)
        try:
            stat = models.Statistics.objects.get(shelf=shelf, day=day)
            stats_count += 1
            disp = stat.sold_count - stat.sold_count * relevance
            max_for_day_sum += stat.sold_count + disp
            min_for_day_sum += stat.sold_count - disp
        except models.Statistics.DoesNotExist:
            pass
        relevance = (2**(days_count - i - 1))/(2**days_count)
    min_recommended = 0
    max_recommended = 0
    if stats_count != 0:
        min_recommended = math.floor(min_for_day_sum / stats_count)
        max_recommended = math.ceil(max_for_day_sum / stats_count)
        years_to_count += 1
    if min_recommended < min_products_count:
        min_recommended = min_products_count
    if max_recommended > max_products_count:
        max_recommended = max_products_count

    # 3. Last year borders

    calculatedStats = calculateLastYearStats(
        currentDate, shelf, min_products_count, max_products_count, years_to_count, 365
    )
    min_year_ago = calculatedStats[0]
    max_year_ago = calculatedStats[1]
    years_to_count = calculatedStats[2]

    # 4. Two years ago borders

    calculatedStats = calculateLastYearStats(
        currentDate, shelf, min_products_count, max_products_count, years_to_count, 365 * 2
    )
    min_two_years_ago = calculatedStats[0]
    max_two_years_ago = calculatedStats[1]
    years_to_count = calculatedStats[2]

    # 5. Result

    min_final = math.ceil((min_products_count + min_recommended +
                           min_year_ago + min_two_years_ago) / years_to_count)
    max_final = math.floor((max_products_count + max_recommended +
                            max_year_ago + max_two_years_ago) / years_to_count)
    avg_recommended = math.ceil(
        ((min_final + max_final)/2 + products_count_average)/2)
    return [min_final, max_final, avg_recommended]


def calculateNextDay(payload):
    result = helpers.getEmptyResultObject()

    statsJSON = "{"
    storeElems = models.Store.objects.all()
    for shelf in storeElems:
        shelfStats = getStatsForShelf(shelf)

        min_final = shelfStats[0]
        max_final = shelfStats[1]
        avg_recommended = shelfStats[2]

        statsJSON += '"' + str(shelf.id) + '":{"min_products":"' + str(min_final) + '", "max_products": "' + str(
            max_final) + '", "avg_recommended":"' + str(avg_recommended) + '"},'

    result['success'] = statsJSON[:-1] + '}'
    return result
