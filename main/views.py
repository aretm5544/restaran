from rest_framework import viewsets
from .models import Restaurant, Dish, Beverage
from .serializers import RestaurantSerializer, DishSerializer, BeverageSerializer
from rest_framework import filters


class RestaurantFilter(filters.FilterSet):
    is_vegetarian = filters.BooleanFilter(field_name='dishes__is_vegetarian', lookup_expr='exact')

    class Meta:
        model = Restaurant
        fields = ['is_vegetarian']

class RestaurantViewSet(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    filterset_class = RestaurantFilter

class RestaurantViewSet(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

class DishViewSet(viewsets.ModelViewSet):
    queryset = Dish.objects.all()
    serializer_class = DishSerializer

class BeverageViewSet(viewsets.ModelViewSet):
    queryset = Beverage.objects.all()
    serializer_class = BeverageSerializer