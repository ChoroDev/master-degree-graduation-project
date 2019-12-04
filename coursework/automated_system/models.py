from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=20)
    price = models.FloatField()
    production_date = models.DateTimeField()
    expiration_days = models.IntegerField()
    product_type = models.CharField(max_length=20, default="None")


class CargoTransportation(models.Model):
    company_name = models.CharField(max_length=100)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    delivered_count = models.IntegerField()
    delivery_date = models.DateTimeField()


class Storage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    product_count = models.IntegerField()
    delivery = models.ForeignKey(CargoTransportation, on_delete=models.CASCADE)


class Store(models.Model):
    shelf_number = models.IntegerField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)


class Staff(models.Model):
    name = models.CharField(max_length=40)
    surname = models.CharField(max_length=40)
    position = models.CharField(max_length=50)


class Equipment(models.Model):
    name = models.CharField(max_length=20)
    equipment_type = models.CharField(max_length=20, default="None")
    cost = models.FloatField()
    last_maintainance_date = models.DateTimeField()
    warranty_period_years = models.IntegerField()
