from django.forms import ModelForm
from . import models


class ProductForm(ModelForm):
    class Meta:
        model = models.Product
        fields = {'name', 'product_type'}