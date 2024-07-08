from typing import Any, Sequence
from django.core.management import BaseCommand
from shopapp.models import Order, Product
from django.contrib.auth.models import User


# class Command(BaseCommand):
#     def handle(self, *args: Any, **options: Any) -> str | None:
#         self.stdout.write("Start demo select fields")
#         products_values = Product.objects.values("pk", "name")

#         for p_values in products_values:
#             print(p_values)
#         self.stdout.write("Done")


class Command(BaseCommand):
    def handle(self, *args: Any, **options: Any) -> str | None:
        self.stdout.write("Start demo select fields")
        users_info = User.objects.values_list("username", flat=True)
        print(list(users_info))
        for user_info in users_info:
            print(user_info)
        self.stdout.write("Done")
