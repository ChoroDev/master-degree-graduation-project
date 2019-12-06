from .. import models
from datetime import datetime


def fill_in_product():
    models.Product.objects.create(name="Apple", price=1.0, production_date=datetime.now(
    ), expiration_days=60, product_type="Food")
    models.Product.objects.create(name="Pineapple", price=1.2, production_date=datetime.now(
    ), expiration_days=60, product_type="Food")
    models.Product.objects.create(name="Orange Juice", price=1.1, production_date=datetime.now(
    ), expiration_days=180, product_type="Food")
    models.Product.objects.create(name="Milk", price=0.9, production_date=datetime.now(
    ), expiration_days=3, product_type="Food")
    models.Product.objects.create(name="Carrot", price=0.6, production_date=datetime.now(
    ), expiration_days=60, product_type="Food")
    models.Product.objects.create(name="Cucumber", price=0.3, production_date=datetime.now(
    ), expiration_days=60, product_type="Food")
    models.Product.objects.create(name="Potato", price=0.2, production_date=datetime.now(
    ), expiration_days=60, product_type="Food")
    models.Product.objects.create(name="Tomato", price=0.4, production_date=datetime.now(
    ), expiration_days=60, product_type="Food")


def fill_in_cargo():
    models.CargoTransportation.objects.create(
        company_name="Food Delivery", delivered_count=500, delivery_date=datetime.now(), product_id=1)
    models.CargoTransportation.objects.create(
        company_name="Food Delivery", delivered_count=500, delivery_date=datetime.now(), product_id=2)
    models.CargoTransportation.objects.create(
        company_name="Food Delivery", delivered_count=500, delivery_date=datetime.now(), product_id=5)
    models.CargoTransportation.objects.create(
        company_name="Food Delivery", delivered_count=500, delivery_date=datetime.now(), product_id=6)
    models.CargoTransportation.objects.create(
        company_name="Food Delivery", delivered_count=500, delivery_date=datetime.now(), product_id=7)
    models.CargoTransportation.objects.create(
        company_name="Food Delivery", delivered_count=500, delivery_date=datetime.now(), product_id=8)
    models.CargoTransportation.objects.create(
        company_name="Juicy Liquids", delivered_count=500, delivery_date=datetime.now(), product_id=3)
    models.CargoTransportation.objects.create(
        company_name="Happy Milk Farm", delivered_count=500, delivery_date=datetime.now(), product_id=4)


def fill_in_storage():
    models.Storage.objects.create(
        product_count=1000, delivery_id=1, product_id=1)
    models.Storage.objects.create(
        product_count=1500, delivery_id=2, product_id=2)
    models.Storage.objects.create(
        product_count=560, delivery_id=3, product_id=3)
    models.Storage.objects.create(
        product_count=1100, delivery_id=4, product_id=4)
    models.Storage.objects.create(
        product_count=2300, delivery_id=5, product_id=5)
    models.Storage.objects.create(
        product_count=700, delivery_id=6, product_id=6)
    models.Storage.objects.create(
        product_count=800, delivery_id=7, product_id=7)
    models.Storage.objects.create(
        product_count=550, delivery_id=8, product_id=8)


def fill_in_store():
    models.Store.objects.create(shelf_number=1, product_id=1)
    models.Store.objects.create(shelf_number=2, product_id=2)
    models.Store.objects.create(shelf_number=3, product_id=3)
    models.Store.objects.create(shelf_number=4, product_id=4)
    models.Store.objects.create(shelf_number=5, product_id=5)
    models.Store.objects.create(shelf_number=6, product_id=6)
    models.Store.objects.create(shelf_number=7, product_id=7)
    models.Store.objects.create(shelf_number=8, product_id=8)


def fill_in_staff():
    models.Staff.objects.create(
        name="John", surname="Doe", position="Business manager")
    models.Staff.objects.create(
        name="Jane", surname="Doe", position="Store manager")
    models.Staff.objects.create(
        name="Mike", surname="Smith", position="Merchandizer")
    models.Staff.objects.create(
        name="Tom", surname="Heinz", position="Merchandizer")
    models.Staff.objects.create(
        name="Hacker", surname="Man", position="System administrator")
    models.Staff.objects.create(
        name="Vasya", surname="Sidorov", position="Driver")


def fill_in_equipment():
    models.Equipment.objects.create(name="Automated System", equipment_type="Enterprise",
                                    cost="99999.9", last_maintainance_date=datetime.now(), warranty_period_years=228)
    models.Equipment.objects.create(name="Shelf 1", equipment_type="Store Component",
                                    cost="150.5", last_maintainance_date=datetime.now(), warranty_period_years=228)
    models.Equipment.objects.create(name="Shelf 2", equipment_type="Store Component",
                                    cost="150.5", last_maintainance_date=datetime.now(), warranty_period_years=228)
    models.Equipment.objects.create(name="Shelf 3", equipment_type="Store Component",
                                    cost="150.5", last_maintainance_date=datetime.now(), warranty_period_years=228)
    models.Equipment.objects.create(name="Shelf 4", equipment_type="Store Component",
                                    cost="150.5", last_maintainance_date=datetime.now(), warranty_period_years=228)
    models.Equipment.objects.create(name="Shelf 5", equipment_type="Store Component",
                                    cost="150.5", last_maintainance_date=datetime.now(), warranty_period_years=228)
    models.Equipment.objects.create(name="Shelf 6", equipment_type="Store Component",
                                    cost="150.5", last_maintainance_date=datetime.now(), warranty_period_years=228)
    models.Equipment.objects.create(name="Shelf 7", equipment_type="Store Component",
                                    cost="150.5", last_maintainance_date=datetime.now(), warranty_period_years=228)
    models.Equipment.objects.create(name="Shelf 8", equipment_type="Store Component",
                                    cost="150.5", last_maintainance_date=datetime.now(), warranty_period_years=228)
    models.Equipment.objects.create(name="Truck", equipment_type="Car",
                                    cost="6500.2", last_maintainance_date=datetime.now(), warranty_period_years=10)


def remove_product():
    models.Product.objects.filter(id=1).delete()


def update_store():
    models.Store.objects.filter(id=1).update(product_count=10)


def get_current_status():
    return "OK"
