from .. import models
from datetime import datetime
from datetime import date
from datetime import timedelta


def fill_in_products():
    models.Product.objects.create(
        name="Apple",
        digit_code="00000-0001",
        shelf_life=(datetime.now() + timedelta(days=365)),
        width=200.0,
        height=100.0,
        length=150.0,
        weight=500.0,
        price=2.1,
        stackable=True)
    models.Product.objects.create(
        name="Pineapple",
        digit_code="00000-0002",
        shelf_life=(datetime.now() + timedelta(days=365)),
        width=150.0,
        height=300.0,
        length=150.0,
        weight=1500.0,
        price=1.1,
        stackable=True)
    models.Product.objects.create(
        name="Orange Juice",
        digit_code="00000-0003",
        shelf_life=(datetime.now() + timedelta(days=365)),
        width=100.0,
        height=200.0,
        length=50.0,
        weight=1000.0,
        price=1.2,
        stackable=True)
    models.Product.objects.create(
        name="Milk",
        digit_code="00000-0004",
        shelf_life=(datetime.now() + timedelta(days=365)),
        width=100.0,
        height=200.0,
        length=50.0,
        weight=950.0,
        price=0.9,
        stackable=True)
    models.Product.objects.create(
        name="Carrot",
        digit_code="00000-0005",
        shelf_life=(datetime.now() + timedelta(days=365)),
        width=90.0,
        height=60.0,
        length=150.0,
        weight=500.0,
        price=1.5,
        stackable=True)
    models.Product.objects.create(
        name="Cucumber",
        digit_code="00000-0007",
        shelf_life=(datetime.now() + timedelta(days=365)),
        width=80.0,
        height=80.0,
        length=100.0,
        weight=500.0,
        price=1.3,
        stackable=True)
    models.Product.objects.create(
        name="Potato",
        digit_code="00000-0008",
        shelf_life=(datetime.now() + timedelta(days=365)),
        width=150.0,
        height=75.0,
        length=80.0,
        weight=500.0,
        price=1.1,
        stackable=True)
    models.Product.objects.create(
        name="Tomato",
        digit_code="00000-0009",
        shelf_life=(datetime.now() + timedelta(days=365)),
        width=200.0,
        height=100.0,
        length=50.0,
        weight=500.0,
        price=1.4,
        stackable=True)


def fill_in_storage():
    models.Storage.objects.create(
        product=models.Product.objects.get(name='Apple'),
        product_count=100)
    models.Storage.objects.create(
        product=models.Product.objects.get(name='Pineapple'),
        product_count=25)
    models.Storage.objects.create(
        product=models.Product.objects.get(name='Orange Juice'),
        product_count=50)
    models.Storage.objects.create(
        product=models.Product.objects.get(name='Milk'),
        product_count=30)
    models.Storage.objects.create(
        product=models.Product.objects.get(name='Carrot'),
        product_count=40)
    models.Storage.objects.create(
        product=models.Product.objects.get(name='Cucumber'),
        product_count=35)
    models.Storage.objects.create(
        product=models.Product.objects.get(name='Potato'),
        product_count=50)
    models.Storage.objects.create(
        product=models.Product.objects.get(name='Tomato'),
        product_count=40)


# def fill_in_cargo():
#     models.CargoTransportation.objects.create(
#         company_name="Food Delivery", delivered_count=500, delivery_date=datetime.now(), product_id=1)
#     models.CargoTransportation.objects.create(
#         company_name="Food Delivery", delivered_count=500, delivery_date=datetime.now(), product_id=2)
#     models.CargoTransportation.objects.create(
#         company_name="Food Delivery", delivered_count=500, delivery_date=datetime.now(), product_id=5)
#     models.CargoTransportation.objects.create(
#         company_name="Food Delivery", delivered_count=500, delivery_date=datetime.now(), product_id=6)
#     models.CargoTransportation.objects.create(
#         company_name="Food Delivery", delivered_count=500, delivery_date=datetime.now(), product_id=7)
#     models.CargoTransportation.objects.create(
#         company_name="Food Delivery", delivered_count=500, delivery_date=datetime.now(), product_id=8)
#     models.CargoTransportation.objects.create(
#         company_name="Juicy Liquids", delivered_count=500, delivery_date=datetime.now(), product_id=3)
#     models.CargoTransportation.objects.create(
#         company_name="Happy Milk Farm", delivered_count=500, delivery_date=datetime.now(), product_id=4)


# def fill_in_store():
#     models.Store.objects.create(shelf_number=1, product_id=1)
#     models.Store.objects.create(shelf_number=2, product_id=2)
#     models.Store.objects.create(shelf_number=3, product_id=3)
#     models.Store.objects.create(shelf_number=4, product_id=4)
#     models.Store.objects.create(shelf_number=5, product_id=5)
#     models.Store.objects.create(shelf_number=6, product_id=6)
#     models.Store.objects.create(shelf_number=7, product_id=7)
#     models.Store.objects.create(shelf_number=8, product_id=8)


# def fill_in_staff():
#     models.Staff.objects.create(
#         name="John", surname="Doe", position="Business manager")
#     models.Staff.objects.create(
#         name="Jane", surname="Doe", position="Store manager")
#     models.Staff.objects.create(
#         name="Mike", surname="Smith", position="Merchandizer")
#     models.Staff.objects.create(
#         name="Tom", surname="Heinz", position="Merchandizer")
#     models.Staff.objects.create(
#         name="Hacker", surname="Man", position="System administrator")
#     models.Staff.objects.create(
#         name="Vasya", surname="Sidorov", position="Driver")


# def fill_in_equipment():
#     models.Equipment.objects.create(name="Automated System", equipment_type="Enterprise",
#                                     cost="99999.9", last_maintainance_date=datetime.now(), warranty_period_years=228)
#     models.Equipment.objects.create(name="Shelf 1", equipment_type="Store Component",
#                                     cost="150.5", last_maintainance_date=datetime.now(), warranty_period_years=228)
#     models.Equipment.objects.create(name="Shelf 2", equipment_type="Store Component",
#                                     cost="150.5", last_maintainance_date=datetime.now(), warranty_period_years=228)
#     models.Equipment.objects.create(name="Shelf 3", equipment_type="Store Component",
#                                     cost="150.5", last_maintainance_date=datetime.now(), warranty_period_years=228)
#     models.Equipment.objects.create(name="Shelf 4", equipment_type="Store Component",
#                                     cost="150.5", last_maintainance_date=datetime.now(), warranty_period_years=228)
#     models.Equipment.objects.create(name="Shelf 5", equipment_type="Store Component",
#                                     cost="150.5", last_maintainance_date=datetime.now(), warranty_period_years=228)
#     models.Equipment.objects.create(name="Shelf 6", equipment_type="Store Component",
#                                     cost="150.5", last_maintainance_date=datetime.now(), warranty_period_years=228)
#     models.Equipment.objects.create(name="Shelf 7", equipment_type="Store Component",
#                                     cost="150.5", last_maintainance_date=datetime.now(), warranty_period_years=228)
#     models.Equipment.objects.create(name="Shelf 8", equipment_type="Store Component",
#                                     cost="150.5", last_maintainance_date=datetime.now(), warranty_period_years=228)
#     models.Equipment.objects.create(name="Truck", equipment_type="Car",
#                                     cost="6500.2", last_maintainance_date=datetime.now(), warranty_period_years=10)


# def remove_product():
#     models.Product.objects.filter(id=1).delete()


# def update_store():
#     models.Store.objects.filter(id=1).update(product_count=9)
#     models.Store.objects.filter(id=2).update(product_count=5)
#     models.Store.objects.filter(id=3).update(product_count=7)
#     models.Store.objects.filter(id=4).update(product_count=5)
#     models.Store.objects.filter(id=5).update(product_count=8)
#     models.Store.objects.filter(id=6).update(product_count=9)
#     models.Store.objects.filter(id=7).update(product_count=9)
#     models.Store.objects.filter(id=8).update(product_count=6)


# def update_store_products(product_id, product_count):
#     models.Store.objects.filter(id=product_id).update(
#         product_count=product_count)


# def update_storage_products(product_id, product_count):
#     models.Storage.objects.filter(id=product_id).update(
#         product_count=product_count)


# def update_references():
#     models.Store.objects.filter(id=1).update(maintainer_id=3)


# def checkStore():
#     statusString = ""
#     status = "fine"
#     shelf = models.Store.objects.all()
#     for product in shelf:
#         currentProduct = models.Product.objects.get(id=product.product_id)
#         if product.product_count < 5:
#             statusString = "Product: " + currentProduct.name + \
#                 ": insufficient count of product on shelf"
#             if status != "error":
#                 status = "warning"
#             print(product.product_count)
#             # externalModule.orderProductFromStorage
#         elif product.product_count == 0:
#             statusString = "Product: " + currentProduct.name + ": shelf is out of this product"
#             status = "error"
#             # externalModule.orderProductFromStorage
#     if not statusString:
#         statusString = "fine"
#     return {"data": "Store: " + statusString + "; ", "status": status}


# def checkStorage():
#     statusString = ""
#     status = "fine"
#     storage = models.Storage.objects.all()
#     for product in storage:
#         currentProduct = models.Product.objects.get(id=product.product_id)
#         if product.product_count < 50:
#             statusString = "Product: " + currentProduct.name + \
#                 ": insufficient count of product in storage"
#             if status != "error":
#                 status = "warning"
#             print(product.product_count)
#             # externalModule.orderProductFromExternal
#         elif product.product_count == 0:
#             statusString = "Product: " + currentProduct.name + \
#                 ": storage is out of this product"
#             status = "error"
#             # externalModule.orderProductFromExternal
#             # externalModule.notifyManagement
#     if not statusString:
#         statusString = "fine"
#     return {"data": "Storage: " + statusString + "; ", "status": status}


# def checkEquipment():
#     statusString = ""
#     status = "fine"
#     equipment = models.Equipment.objects.all()
#     for item in equipment:
#         currentDate = datetime.now()
#         lastMaintainanceYear = item.last_maintainance_date.year
#         warrantyExpirationDate = item.last_maintainance_date.replace(
#             year=lastMaintainanceYear+item.warranty_period_years, tzinfo=None)
#         daysToExpire = abs((currentDate-warrantyExpirationDate).days)
#         if daysToExpire < 30 and daysToExpire > 0:
#             statusString = "Equipment: " + item.name + \
#                 ": warranty is about to expire"
#             if status != "error":
#                 status = "warning"
#             # externalModule.notifyManagement
#         elif daysToExpire < 0:
#             statusString = "Equipment: " + item.name + \
#                 ": warranty expired"
#             status = "error"
#             # externalModule.notifyManagement
#     if not statusString:
#         statusString = "fine"
#     return {"data": "Equipment: " + statusString + "; ", "status": status}


# def get_current_status():
#     storeStatus = checkStore()
#     storageStatus = checkStorage()
#     equipmentStatus = checkEquipment()
#     return {"store": storeStatus, "storage": storageStatus, "equipment": equipmentStatus}


# def get_storage_products():
#     return models.Storage.objects.all()


# def get_storage_products_for_page():
#     storageProduct = []
#     for item in models.Storage.objects.all():
#         product_name = models.Product.objects.get(id=item.product_id).name
#         product_count = models.Storage.objects.get(id=item.id).product_count
#         last_delivery = models.CargoTransportation.objects.get(
#             id=item.delivery_id).delivery_date
#         image_name = product_name.lower().replace(' ', '_')
#         storageProduct.append({"product_name": product_name, "product_count": product_count,
#                                "last_delivery": last_delivery, "image_name": image_name})
#     return storageProduct


# def get_store_products():
#     return models.Store.objects.all()


# def get_transportations_info():
#     transpos = []
#     for transp in models.CargoTransportation.objects.all():
#         product_name = models.Product.objects.get(id=transp.product_id).name
#         transpos.append({"product_name": product_name, "company_name": transp.company_name,
#                          "delivery_date": transp.delivery_date, "delivered_count": transp.delivered_count})
#     return transpos
