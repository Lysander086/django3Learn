from django.http import JsonResponse

from .models import Product, Manufacturer


def product_list(request):
    products = Product.objects.all()  # [:30]
    data = {"products": list(products.values("pk", "name"))}
    response = JsonResponse(data)
    return response


def product_detail(request, pk):
    try:
        product = Product.objects.get(pk=pk)
        data = {"product": {
            "name": product.name,
            "manufacturer": product.manufacturer,
            "description": product.description,
            "photo": product.photo.url,
            "price": product.price,
            "shipping_cost": product.shipping_cost,
            "quantity": product.quantity,
        }}

        response = JsonResponse(data)

    except Product.DoesNotExist:
        response = JsonResponse({
            "error": {
                "code": 404,
                "message": "product not found"
            }
        }, status=404)

    return response


def manufacturer_list(req):
    manufacturers = Manufacturer.objects.all()
    data = {
        "manufacturers": list(manufacturers.values("pk", "name"))
    }
    res = JsonResponse(data)
    return res


def manufacturer_detail(req, pk):
    try:
        manufacturer = Manufacturer.objects.get(pk=pk)
        data = {"manufacturer": {
            "name": manufacturer.name,
            "location": manufacturer.location,
            "active": manufacturer.active,
        }}

        return JsonResponse(data)

    except Manufacturer.DoesNotExist:
        return JsonResponse({
            "error": {
                "code": 404,
                "message": "not found"
            }
        }, status=404)
