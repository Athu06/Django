# urls.py

from django.urls import path
from .views import signup, signin, ProductListCreateView, UserListCreateView, RecommendationListCreateView

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('signin/', signin, name='signin'),
    path('products/', ProductListCreateView.as_view(), name='product-list-create'),
    path('users/', UserListCreateView.as_view(), name='user-list-create'),
    path('recommendations/', RecommendationListCreateView.as_view(), name='recommendation-list-create'),
]
