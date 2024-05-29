from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.http import HttpResponse, HttpRequest, HttpResponseRedirect, JsonResponse
from django.contrib.auth.models import Group


from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin

from .models import Product, Order, ProductImage
from .forms import ProductForm, GroupForm

from timeit import default_timer

class ShopIndexView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        products_list_tupl = [
            ('tea', 20),
            ('coffee', 35),
            ('milk', 10),
        ]
        context = {
            "time_running": default_timer(),
            "products": products_list_tupl,
            "items": 5,
        }
        return render(request, 'shopapp/shop_page.html', context=context)
    

class GroupsListView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        context = {
            # "groups": Group.objects.all(),
            "form": GroupForm(),
            "groups": Group.objects.prefetch_related('permissions').all(),

        }
        return render(request, 'shopapp/groups-list.html', context=context)
    
    def post(self, request: HttpRequest):
        form = GroupForm(request.POST)
        if form.is_valid():
            form.save()

        return redirect(request.path)


class ProductDetailsView(DetailView):
    template_name = 'shopapp/product-details.html'
    # model = Product
    queryset = Product.objects.prefetch_related("images")
    context_object_name = 'product'

    
class ProductListView(ListView):
    template_name = 'shopapp/products-list.html'
    # model = Product
    context_object_name = 'products'
    queryset = Product.objects.filter(archived=False)


class ProductCreateView(UserPassesTestMixin, CreateView):
    # def test_func(self) -> bool | None:
    #     # return self.request.user.groups.filter(name='secret-group').exists()
    #     return self.request.user.is_superuser
    model = Product
    fields = "name", "price", "description", "discount", "preview"
    success_url = reverse_lazy('shopapp:products_list')

    
class ProductUpdateView(UpdateView):
    model = Product
    # fields = "name", "price", "description", "discount", "preview"
    template_name_suffix = "_update_form"
    form_class = ProductForm

    def get_success_url(self) -> str:
        return reverse(
            "shopapp:product_details",
            kwargs={"pk": self.object.pk}
        )
    
    def form_valid(self, form):
        response = super().form_valid(form)

        if form.files.getlist("images"):
            # Delete existing images
            self.object.images.all().delete()
            
            # Create new images
            for image in form.files.getlist("images"):
                ProductImage.objects.create(
                    product=self.object,
                    image=image,
                )

        return response


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('shopapp:products_list')

    def form_valid(self, form):
        success_url = self.get_success_url()
        self.object.archived = True
        self.object.save()
        return HttpResponseRedirect(success_url)


class OrdersListView(LoginRequiredMixin,ListView):
    queryset = (
        Order.objects
        .select_related("user")
        .prefetch_related("products")
        )
    
class OrderDetailView(PermissionRequiredMixin, DetailView):
    permission_required = ["shopapp.view_order"]
    queryset = (
        Order.objects
        .select_related("user")
        .prefetch_related("products")
        )
    
class ProductsDataExportView(View):
    def get(self, request: HttpRequest) -> JsonResponse:
        products = Product.objects.order_by("pk").all()
        products_data = [
            {
                'pk': product.pk,
                'name': product.name,
                'price': product.price,
                'archived': product.archived,
            }
            for product in products
        ]
        return JsonResponse({"products": products_data})