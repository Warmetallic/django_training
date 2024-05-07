"""
Django Admin Integration
"""
from django.contrib import admin
from django.db.models import QuerySet
from django.http import HttpRequest

from .models import Product, Order, ProductImage

from .admin_mixins import ExportAsCSVMixin



class OrderInline(admin.StackedInline):
    model = Product.orders.through

class ProductInline(admin.TabularInline):
    model = ProductImage

@admin.action(description="Archive products")
def mark_archived(modeladmin: admin.ModelAdmin, request: HttpRequest, queryset: QuerySet):
    queryset.update(archived=True)


@admin.action(description="Unarchive products")
def unmark_archived(modeladmin: admin.ModelAdmin, request: HttpRequest, queryset: QuerySet):
    queryset.update(archived=False)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin, ExportAsCSVMixin):
    """
    Product Model Administration
    """
    actions = [
        mark_archived,
        unmark_archived,
        "export_csv",
    ]

    inlines = [
        OrderInline,
        ProductInline,
    ]
    #     list_display = ("pk", "name", "description", "price", "discount")
    list_display = ("pk", "name", "description_short", "price", "discount", "archived")
    list_display_links = ("pk", "name")
    ordering = "-name", "pk" 
    search_fields = "name", "description",
    fieldsets = [
        (None, {"fields": ("name", "description", )}),
        ("Price_options", {
            "fields": ("price", "discount"),
            # "classes": ("collapse",),
        }),
        ("Images", {
            "fields":("preview",),
        }),
        ("Extra options", {
            "fields":("archived",),
            "classes":("collapse",),
            "description":"Extra options. Field 'archived' is for soft delete.",
        })
    ]


    def description_short(self, obj: Product) -> str:
        if len(obj.description) < 48:
            return obj.description
        return obj.description[:48] + "..."


# admin.site.register(Product, ProductAdmin)
    

class ProductInline(admin.StackedInline):
    model = Order.products.through


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines =  [
        ProductInline,
    ]

    list_display = ("delivery_address", "promocode", "created_at", "user_verbose")

    def get_queryset(self, request):
        return Order.objects.select_related("user").prefetch_related("products")
    
    def user_verbose(self, obj: Order) -> str:
        return obj.user.first_name or obj.user.username