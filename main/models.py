from django.db import models

class Restaurant(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    rating = models.FloatField()
    type_of_kitchen = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Dish(models.Model):
    name = models.CharField(max_length=200)
    ingredients = models.TextField()
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    price = models.FloatField()
    is_vegetarian = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Beverage(models.Model):
    name = models.CharField(max_length=200)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    type = models.CharField(max_length=200)
    volume = models.FloatField()
    price = models.FloatField()

    def __str__(self):
        return self.name