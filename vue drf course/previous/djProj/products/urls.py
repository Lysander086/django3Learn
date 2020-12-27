from django.urls import path

from .views import product_detail, manufacturer_detail,manufacturer_list
from .views import product_list

urlpatterns = [
    path("products/", product_list, name="product-list"),
    path("products/<int:pk>/", product_detail, name="product-detail"),
    path("manufacturers/", manufacturer_list, name="manufacturer_list"),
    path("manufacturers/<int:pk>/", manufacturer_detail, name="manufacturer_detail"),

]
