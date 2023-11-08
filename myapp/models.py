from django.db import models
from django.contrib import admin 

class student(models.Model):   
    id = models.AutoField(primary_key=True)
    Fullname = models.CharField(max_length=50)
    DOB = models.DateField()
    Email = models.EmailField(max_length=50)
    Age = models.BigIntegerField()
    Gender = models.CharField(max_length=50)
    Country = models.CharField(max_length=50)
    State = models.CharField(max_length=50)
    City = models.CharField(max_length=50)
    Qualification =models.CharField(max_length=50)
    Subject = models.CharField(max_length=100)
    Password = models.CharField(max_length=100)
    def __str__(self) -> str:
        return self.Fullname

class Country(models.Model):
    country_name = models.CharField(max_length=50)
    country_value = models.CharField(max_length=10)
    phonecode = models.CharField(max_length=10)

    def __str__(self):
        return self.country_name


class State(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE, null=True)
    state_name = models.CharField(max_length=50)

    def __str__(self):
        return self.state_name


class City(models.Model):
    state = models.ForeignKey(State, on_delete=models.CASCADE, null=True)
    city_name = models.CharField(max_length=50)
    def __str__(self):
        return self.city_name
