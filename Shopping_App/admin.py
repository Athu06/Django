from django.contrib import admin

from django.contrib import admin
from .models import Product, User, Recommendation

admin.site.register(Product)
admin.site.register(User)
admin.site.register(Recommendation)
