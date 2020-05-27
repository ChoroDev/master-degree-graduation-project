from django.db import models
from django.contrib.auth.models import User as BaseUser
from django.db.models.signals import post_save
from django.dispatch import receiver
import json


class User(models.Model):
    user = models.OneToOneField(
        BaseUser, parent_link=True, related_name='profile', null=True, on_delete=models.CASCADE)
    USER_GROUPS = (
        ('P', 'Personel'),
        ('M', 'Management'),
        ('A', 'SystemAdministrators')
    )
    group = models.CharField(max_length=1, choices=USER_GROUPS, default='P')

    def toJSON(self):
        user = BaseUser.objects.get(profile=self)
        return ('{ '
                + '"id": "' + str(self.id)
                + '", "group": "' + str(self.group)
                + '", "first_name": "' + str(user.first_name)
                + '", "last_name": "' + str(user.last_name)
                + '", "email": "' + str(user.email)
                + '"}')


@receiver(post_save, sender=BaseUser)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        User.objects.create(user=instance)


@receiver(post_save, sender=BaseUser)
def save_profile(sender, instance, created, **kwargs):
    profile = User.objects.get_or_create(user=instance)[0]
    userGroups = list()
    for group in instance.groups.all():
        userGroups.append(group.name)
    if userGroups:
        if userGroups[0] == "SystemAdministrators":
            profile.group = 'A'
        elif userGroups[0] == "Management":
            profile.group = 'M'
        else:
            profile.group = 'P'
    profile.save()


class Failure(models.Model):
    text = models.TextField(blank=True)
    severity = models.IntegerField(default=1)
    timestamp = models.DateTimeField(auto_now=True)
    possible_cause = models.TextField(blank=True)
    possible_solution = models.TextField(blank=True)
    stack_trace = models.TextField(blank=True)
    is_solved = models.BooleanField(default=False)
    assignee = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def toJSON(self):
        return ('{ '
                + '"id": "' + str(self.id)
                + '", "severity": "' + str(self.severity)
                + '", "timestamp": "' + str(self.timestamp)
                + '", "possible_cause": "' + str(self.possible_cause)
                + '", "possible_solution": "' + str(self.possible_solution)
                + '", "stack_trace": "' + str(self.stack_trace)
                + '", "is_solved": "' + str(self.is_solved)
                + '", "assignee_id": "' +
                str((self.assignee and self.assignee.id) or "")
                + '"}')


class Product(models.Model):
    name = models.CharField(max_length=30, blank=True)
    digit_code = models.CharField(max_length=9, blank=True)
    shelf_life = models.IntegerField(default=0)
    width = models.FloatField(default=0.0)
    height = models.FloatField(default=0.0)
    length = models.FloatField(default=0.0)
    weight = models.FloatField(default=0.0)
    price = models.FloatField(default=0.0)
    stackable = models.BooleanField(default=False)

    def toJSON(self):
        return('{ '
               + '"id": "' + str(self.id)
               + '", "name": "' + str(self.name)
               + '", "digit_code": "' + str(self.digit_code)
               + '", "shelf_life": "' + str(self.shelf_life)
               + '", "width": "' + str(self.width)
               + '", "height": "' + str(self.height)
               + '", "length": "' + str(self.length)
               + '", "weight": "' + str(self.weight)
               + '", "price": "' + str(self.price)
               + '", "stackable": "' + str(self.stackable)
               + '"}')


class Storage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    product_count = models.IntegerField(default=0)
    delivery_timestamp = models.DateTimeField(null=True)

    def toJSON(self):
        return ('{ '
                + '"id": "' + str(self.id)
                + '", "product_id": "' + str(self.product.id)
                + '", "product_count": "' + str(self.product_count)
                + '", "delivery_timestamp": "' + str(self.delivery_timestamp)
                + '"}')


class Store(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    product_count = models.IntegerField(default=0)
    width = models.FloatField(default=0.0)
    height = models.FloatField(default=0.0)
    length = models.FloatField(default=0.0)
    carrying_capacity = models.FloatField(default=0.0)
    shelf_name = models.CharField(max_length=30, blank=True)
    section_name = models.CharField(max_length=30, blank=True)
    last_charge = models.DateTimeField(auto_now=True)

    def toJSON(self):
        return ('{ '
                + '"id": "' + str(self.id)
                + '", "product_id": "' + str(self.product.id)
                + '", "profile_id": "' +
                str((self.user and self.user.id) or "")
                + '", "product_count": "' + str(self.product_count)
                + '", "width": "' + str(self.width)
                + '", "height": "' + str(self.height)
                + '", "length": "' + str(self.length)
                + '", "carrying_capacity": "' + str(self.carrying_capacity)
                + '", "shelf_name": "' + str(self.shelf_name)
                + '", "section_name": "' + str(self.section_name)
                + '", "last_charge": "' + str(self.last_charge)
                + '"}')


class Stock(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    stock_price = models.FloatField(default=0.0)
    start_timestamp = models.DateTimeField()
    end_timestamp = models.DateTimeField()


class Statistics(models.Model):
    day = models.DateField(null=True)
    shelf = models.ForeignKey(Store, on_delete=models.CASCADE)
    sold_count = models.IntegerField(default=0)
    stock = models.ForeignKey(Stock, on_delete=models.SET_NULL, null=True)
    failures_count = models.IntegerField(default=0)
    price_that_day = models.FloatField(default=0.0)

    @property
    def statYear(self):
        "Returns year of statistic record"
        return self.day.strftime('%Y')

    def toJSON(self):
        return ('{ '
                + '"id": "' + str(self.id)
                + '", "day": "' + str(self.day)
                + '", "shelf_id": "' + str(self.shelf.id)
                + '", "sold_count": "' + str(self.sold_count)
                + '", "stock_id": "' +
                str((self.stock and self.stock.id) or "")
                + '", "failures_count": "' + str(self.failures_count)
                + '", "price_that_day": "' + str(self.price_that_day)
                + '"}')
