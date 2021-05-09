from django import forms
from django.forms import widgets
from products.models import Product

class ProductForm(forms.ModelForm):
    
    class Meta:
        model = Product
        fields = '__all__'

        labels = {
            'imgurl': 'Image URL'
        }

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Product name'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Describe the product'
            }),
            'imgurl': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'URL of image',
                'label': 'Image URL'
            }),
            'price': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Price of product',
                'type': 'number'
            }),
        }   