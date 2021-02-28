from django.contrib import admin

# Register your models here.
from .models import PizzaSpecification, PizzaInstantiation
admin.site.register([PizzaSpecification, PizzaInstantiation])
