from django.db import models


# Create your models here.
class Dish(models.Model):
    name = models.CharField(max_length=50)
    products = models.ManyToManyField('Product', through='Recipe')

    def __str__(self):
        return self.name


class ProductType(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=50)
    product_type = models.ForeignKey(ProductType, on_delete=models.SET_NULL, null=True)
    dishes = models.ManyToManyField(Dish, through='Recipe')

    def __str__(self):
        return self.name


class Recipe(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=6, decimal_places=3)

    def __str__(self):
        return self.dish.name + '/' + self.product.name + ' (' + str(self.quantity) + ')'


# РАБОТАЙ ПОЖАЛУЙСТА Я ТЕБЯ ПРОШУ
