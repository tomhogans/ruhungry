from django.db import models
from django.contrib.auth.models import User


class Station(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField()

    def __str__(self):
        return '%s Station' % self.name


class Food(models.Model):
    station = models.ForeignKey('Station')
    name = models.CharField(max_length=255, unique=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    available = models.BooleanField(default=True)
    description = models.TextField()

    def __str__(self):
        return self.name


class Order(models.Model):
    user = models.ForeignKey(User)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.id
