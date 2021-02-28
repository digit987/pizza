from django.db import models
import random

# Create your models here.
class PizzaSpecification(models.Model):
    pizza_size = models.CharField(max_length=30)
    pizza_toppings = models.CharField(max_length=30)

class PizzaInstantiation(models.Model):
    pizza_id = models.AutoField(primary_key=True)
    pizza_type = models.CharField(max_length=20, default=random.choice(['regular', 'square']))
    pizza_size = models.CharField(max_length=30)
    pizza_toppings = models.CharField(max_length=30)
