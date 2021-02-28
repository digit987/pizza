from django.urls import path
from pizza_app import views

urlpatterns = [
    path("pizza_specification", views.PizzaSpecificationView.as_view(), name="pizza_specification"),
    path("pizza_instantiation", views.PizzaInstantiationView.as_view(), name="pizza"),
    path("pizza_instantiation/<int:pizza_id>", views.PizzaInstantiationView.as_view(), name="pizza"),
    path('pizza_instantiation/search_by_type/<str:search_by>', views.PizzaInstantiationView.as_view(), name="search_by_type"),
    path('pizza_instantiation/search_by_size/<str:search_by>', views.PizzaInstantiationView.as_view(), name="search_by_size"),
]
