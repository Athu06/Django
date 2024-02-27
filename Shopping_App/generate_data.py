import random
from django.contrib.auth.models import User
from Shopping_App.models import Product, Recommendation

for _ in range(1000000):
    Product.objects.create(
        shape=random.choice(['circle', 'square', 'triangle']),
        size=random.choice(['small', 'medium', 'large']),
        location=random.choice(['A', 'B', 'C']),
        price=random.uniform(1, 1000)
    )

user1 = User.objects.create(username='user1', password='password1')
user2 = User.objects.create(username='user2', password='password2')

product1 = Product.objects.first()
recommendation1 = Recommendation.objects.create(product=product1, user=user1)

product2 = Product.objects.last()
recommendation2 = Recommendation.objects.create(product=product2, user=user2)

