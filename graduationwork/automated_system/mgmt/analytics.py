from .. import models
from . import helpers
import datetime


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
