from django.db import models


class User(models.Model):
    login = models.CharField(max_length=30)
    password = models.CharField(max_length=100)
    email = models.CharField(max_length=100, blank=True)
    last_access = models.DateTimeField(auto_now=True)
    USER_GROUPS = (
        ('P', 'personel'),
        ('M', 'management'),
        ('A', 'admin')
    )
    group = models.CharField(max_length=1, choices=USER_GROUPS, default='P')


class Statistics(models.Model):
    day = models.DateField(null=True)
    revenue = models.DecimalField(default=0.0, max_digits=30, decimal_places=2)
    sold_count = models.IntegerField(default=0)
    is_stock_day = models.BooleanField(default=False)
    failures_count = models.IntegerField(default=0)


class Failure(models.Model):
    text = models.TextField(blank=True)
    severity = models.IntegerField(default=1)
    timestamp = models.DateTimeField(auto_now=True)
    possible_cause = models.TextField(blank=True)
    possible_solution = models.TextField(blank=True)
    stack_trace = models.TextField(blank=True)
    is_solved = models.BooleanField(default=False)
    assignee = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)


class Product(models.Model):
    name = models.CharField(max_length=30, blank=True)
    digit_code = models.CharField(max_length=9, blank=True)
    shelf_life = models.DateTimeField(null=True)
    width = models.FloatField(default=0.0)
    height = models.FloatField(default=0.0)
    length = models.FloatField(default=0.0)
    weight = models.FloatField(default=0.0)
    price = models.FloatField(default=0.0)
    stackable = models.BooleanField(default=False)


class Storage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    product_count = models.IntegerField(default=0)
    delivery_timestamp = models.DateTimeField(auto_now=True)


class Sales(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    sold_price = models.FloatField(default=0.0)
    sold_date = models.DateTimeField(auto_now=True)
    sold_count = models.IntegerField(default=0)


class Store(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    product_count = models.IntegerField(default=0)
    width = models.FloatField(default=0.0)
    height = models.FloatField(default=0.0)
    length = models.FloatField(default=0.0)
    carrying_capacity = models.FloatField(default=0.0)
    shelf_name = models.CharField(max_length=30, blank=True)
    section_name = models.CharField(max_length=30, blank=True)
    last_charge = models.DateTimeField(auto_now=True)


class Stock(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    shelf = models.ForeignKey(Store, on_delete=models.SET_NULL, null=True)
    stock_price = models.FloatField(default=0.0)
    start_timestamp = models.DateTimeField(auto_now=True)
    end_timestamp = models.DateTimeField()
