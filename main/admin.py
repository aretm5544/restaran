from django.contrib import admin
from .models import Restaurant, Dish, Beverage

class DishInline(admin.TabularInline):
    model = Dish
    extra = 0

class BeverageInline(admin.TabularInline):
    model = Beverage
    extra = 0

class RestaurantAdmin(admin.ModelAdmin):
    inlines = [DishInline, BeverageInline]

admin.site.register(Restaurant, RestaurantAdmin)
admin.site.register(Dish)
admin.site.register(Beverage)