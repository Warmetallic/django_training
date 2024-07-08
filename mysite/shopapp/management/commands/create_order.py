from django.core.management import BaseCommand
from django.contrib.auth.models import User

from shopapp.models import Order, Product
from typing import Sequence
from django.db import transaction


class Command(BaseCommand):
    @transaction.atomic
    def handle(self, *args, **kwargs):
        # with transaction.atomic():
        #     ...
        self.stdout.write("Create order")
        user = User.objects.get(username="admin")
        # products: Sequence[Product] = Product.objects.defer(
        #     "description", "price", "created_at"
        # ).all()
        products: Sequence[Product] = Product.objects.only("id").all()
        order, created = Order.objects.get_or_create(
            delivery_address="Some Street 2",
            promocode="promo4",
            user=user,
        )
        for product in products:
            order.products.add(product)

        order.save()

        self.stdout.write(f"Created order {order}")
