from django.core.management.base import BaseCommand, CommandError
from shopapp.models import Order, Product
from django.db.models import Count, Sum, Avg, Max, Min, F, Q


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write("Start aggregation")
        result = Product.objects.filter(name__contains="Smartphone").aggregate(
            Max("price"),
            min_price=Min("price"),
            average_price=Avg("price"),
            count=Count("id"),
        )
        print(result)
        orders = Order.objects.annotate(
            total=Sum("products__price", default=0),
            products_count=Count("products"),
        )
        for order in orders:
            print(
                f"Order {order.id} total: {order.total}, products count: {order.products_count}"
            )

        self.stdout.write("Done")
