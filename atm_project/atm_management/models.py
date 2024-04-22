from django.db import models
from django.core.serializers.json import DjangoJSONEncoder
import json

class State(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class City(models.Model):
    name = models.CharField(max_length=100)
    state = models.ForeignKey(State, on_delete=models.CASCADE, related_name='cities')

    def __str__(self):
        return f"{self.name}, {self.state}"

class ATMSite(models.Model):
    name = models.CharField(max_length=100)
    site_id = models.CharField(max_length=50, unique=True)
    address = models.CharField(max_length=255)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    contact_details = models.JSONField(encoder=DjangoJSONEncoder)

    def __str__(self):
        return self.name
