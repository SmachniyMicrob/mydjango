from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Dish)
admin.site.register(ProductType)
admin.site.register(Product)
admin.site.register(Recipe)