# forms.py

from django import forms
from .models import Product, User, Recommendation

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'

class RecommendationForm(forms.ModelForm):
    class Meta:
        model = Recommendation
        fields = '__all__'
