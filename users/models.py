from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator

class User(AbstractUser):
    working_hours = models.TimeField()
    age = models.PositiveIntegerField(validators=[MinValueValidator(16), MaxValueValidator(45)])
