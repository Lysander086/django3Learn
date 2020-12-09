from django.http import JsonResponse
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .models import Product, Manufacturer


def product_list(request):
    products = Product.objects.all()  # [:30]
    data = {"products": list(products.values("pk", "name"))}
    response = JsonResponse(data)
    return response


# class ProductDetailView(DetailView):
#     model = Product
#     template_name = 'products/product_detail.html'
#
#
# class ProductListView(ListView):
#     model = Product
#     template_name = 'products/product_list.html'
