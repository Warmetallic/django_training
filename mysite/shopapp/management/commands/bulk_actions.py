from typing import Any, Sequence
from django.core.management import BaseCommand
from shopapp.models import Order, Product
from django.contrib.auth.models import User


class Command(BaseCommand):
    def handle(self, *args: Any, **options: Any) -> str | None:
        self.stdout.write("Start demo bulk actions")

        result = Product.objects.filter(
            name__contains="Smartphone",
        ).update(discount=10)

        print(result)

        # info = [
        #     ("Smartphone1", 100),
        #     ("Smartphone2", 200),
        #     ("Smartphone3", 300),
        # ]

        # products = [Product(name=name, price=price) for name, price in info]

        # result = Product.objects.bulk_create(products)

        # for obj in result:
        #     print(obj)

        self.stdout.write("Done")
