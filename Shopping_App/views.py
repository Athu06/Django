# views.py

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login
from rest_framework import generics
from .models import Product, User, Recommendation
from .forms import ProductForm, UserForm, RecommendationForm
from .serializers import ProductSerializer, UserSerializer, RecommendationSerializer

# Authentication views
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')  # Redirect to your home page
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def signin(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('home')  # Redirect to your home page
    else:
        form = AuthenticationForm()
    return render(request, 'signin.html', {'form': form})

# CRUD views for products, users, and recommendations
# (Assuming you have similar views for Product, User, and Recommendation)

# Product views
def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})

# ... Other product views ...

# User views
def user_list(request):
    users = User.objects.all()
    return render(request, 'user_list.html', {'users': users})

# ... Other user views ...

# Recommendation views
def recommendation_list(request):
    recommendations = Recommendation.objects.all()
    return render(request, 'recommendation_list.html', {'recommendations': recommendations})

# ... Other recommendation views ...

# REST API views using Django Rest Framework
class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class UserListCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class RecommendationListCreateView(generics.ListCreateAPIView):
    queryset = Recommendation.objects.all()
    serializer_class = RecommendationSerializer
