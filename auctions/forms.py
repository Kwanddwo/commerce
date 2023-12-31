from django import forms
from .models import Listing

class ListingForm(forms.ModelForm):
        class Meta:
            model = Listing
            fields = ['name', 
                      'description', 
                      'current_price', 
                      'imageurl', 
                      'category'
                      ]