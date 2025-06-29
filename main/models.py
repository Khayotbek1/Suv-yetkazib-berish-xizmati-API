from django.db import models
from django.core.validators import MinValueValidator
from users.models import User

class Water(models.Model):
    brand = models.CharField(max_length=100)
    price = models.FloatField(validators=[MinValueValidator(0.0)])
    litr = models.FloatField(validators=[MinValueValidator(0.0)])
    description = models.TextField()

    def __str__(self):
        return f"{self.brand} - {self.litr}"


class Client(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=13)
    address = models.TextField()
    debt = models.FloatField(validators=[MinValueValidator(0.0)])

    def __str__(self):
        return f"{self.name} - {self.phone_number}"



class Driver(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=13)
    smena = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} - {self.phone_number}"


class Order(models.Model):
    water = models.ForeignKey(Water, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    admin = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    driver = models.ForeignKey(Driver, on_delete=models.SET_NULL, null=True)

    amount = models.FloatField()
    total_price = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.client.name} - {self.water.brand} - {self.amount} dona"