from django import forms
from .models import Listing

class ListingForm(forms.ModelForm):
    class Meta:
        model = Listing
        fields = [
            'title',
            'price',
            'num_bedrooms',
            'num_bathrooms',
            'square_footage',
            'address',
            'image',  # Add image field here
        ]

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price <= 0:
            raise forms.ValidationError("Price must be a positive number.")
        return price

    def clean_num_bedrooms(self):
        num_bedrooms = self.cleaned_data.get('num_bedrooms')
        if num_bedrooms <= 0:
            raise forms.ValidationError("Number of bedrooms must be a positive number.")
        return num_bedrooms

    def clean_num_bathrooms(self):
        num_bathrooms = self.cleaned_data.get('num_bathrooms')
        if num_bathrooms <= 0:
            raise forms.ValidationError("Number of bathrooms must be a positive number.")
        return num_bathrooms

    def clean_square_footage(self):
        square_footage = self.cleaned_data.get('square_footage')
        if square_footage <= 0:
            raise forms.ValidationError("Square footage must be a positive number.")
        return square_footage
