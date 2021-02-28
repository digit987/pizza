from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.decorators import parser_classes
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404
from django.core import serializers
import json
from pizza_app.models import PizzaSpecification, PizzaInstantiation

class PizzaSpecificationView(APIView):
    @parser_classes([JSONParser])
    def post(self, request):
        pizza_size = request.data.get("pizza_size")
        pizza_toppings = request.data.get("pizza_toppings")

        try:
            pizza_specification = PizzaSpecification(pizza_size=pizza_size, pizza_toppings=pizza_toppings)
            pizza_specification.save()
            return JsonResponse({"success": "Data saved successfully"}, safe=False, status=status.HTTP_201_CREATED)
        except:
            return JsonResponse({"error": "Data couldn't be saved"}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        try:
            pizza_specification = PizzaSpecification.objects.all().values('pizza_size','pizza_toppings')
            return JsonResponse(list(pizza_specification), safe=False)
        except:
            return JsonResponse({"error": "Data couldn't be found"}, status=status.HTTP_400_BAD_REQUEST)

class PizzaInstantiationView(APIView):
    @parser_classes([JSONParser])
    def post(self, request):
        pizza_size = request.data.get("pizza_size")
        pizza_toppings = request.data.get("pizza_toppings")

        try:
            pizza_specification = list(PizzaSpecification.objects.all().values('pizza_size','pizza_toppings'))
            if pizza_size in pizza_specification[0]["pizza_size"] and pizza_toppings in pizza_specification[0]["pizza_toppings"]:
                pizza_instantiation = PizzaInstantiation(pizza_size=pizza_size, pizza_toppings=pizza_toppings)
                pizza_instantiation.save()
                return JsonResponse({"success": "Data saved successfully"}, safe=False, status=status.HTTP_201_CREATED)
            else:
                return JsonResponse({"error": "Pizza with this Size or Topping is not available"}, status=status.HTTP_404_NOT_FOUND)
        except:
            return JsonResponse({"error": "Data couldn't be saved"}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, search_by=None):
        try:
            if search_by:
                try:
                    pizza_instantiation = PizzaInstantiation.objects.filter(pizza_type=search_by).values('pizza_type', 'pizza_size','pizza_toppings')
                    if pizza_instantiation == []:
                        return JsonResponse({"error": "Data couldn't be found"}, status=status.HTTP_404_NOT_FOUND)
                    return JsonResponse(list(pizza_instantiation), safe=False)
                except:
                    return JsonResponse({"error": "Data couldn't be found"}, status=status.HTTP_400_BAD_REQUEST)
                try:
                    pizza_instantiation = PizzaInstantiation.objects.filter(pizza_size=search_by).values('pizza_type', 'pizza_size','pizza_toppings')
                    if pizza_instantiation == []:
                        return JsonResponse({"error": "Data couldn't be found"}, status=status.HTTP_404_NOT_FOUND)
                    return JsonResponse(list(pizza_instantiation), safe=False)
                except:
                    return JsonResponse({"error": "Data couldn't be found"}, status=status.HTTP_400_BAD_REQUEST)
            pizza_instantiation = PizzaInstantiation.objects.all().values('pizza_type', 'pizza_size','pizza_toppings')
            return JsonResponse(list(pizza_instantiation), safe=False)
        except:
            return JsonResponse({"error": "Data couldn't be found"}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pizza_id):
        pizza_size = request.data.get("pizza_size")
        pizza_toppings = request.data.get("pizza_toppings")
        try:
            pizza_specification = list(PizzaSpecification.objects.all().values('pizza_size','pizza_toppings'))
            if pizza_size in pizza_specification[0]["pizza_size"] and pizza_toppings in pizza_specification[0]["pizza_toppings"]:
                pizza_update = PizzaInstantiation.objects.filter(pizza_id=pizza_id).update(pizza_size=pizza_size, pizza_toppings=pizza_toppings)
                return JsonResponse({"success": "Data updated successfully"}, safe=False, status=status.HTTP_201_CREATED)
            else:
                return JsonResponse({"error": "Pizza with this Size or Topping is not available"}, status=status.HTTP_404_NOT_FOUND)
        except:
            return JsonResponse({"error": "Data couldn't be saved"}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pizza_id=None):
        try:
            if pizza_id:
                pizza_delete = PizzaInstantiation.objects.filter(pizza_id=pizza_id).delete()
            else:
                PizzaInstantiation.objects.all().delete()
            return JsonResponse({"success": "Data deleted successfully"}, safe=False, status=status.HTTP_201_CREATED)
        except:
            return JsonResponse({"error": "Data couldn't be deleted"}, status=status.HTTP_400_BAD_REQUEST)
