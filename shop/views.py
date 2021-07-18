from django.shortcuts import render
from requests import request

from .models import Product


# Create your views here.
def index(request):
    product_object = Product.objects.all()
    item_name=request.GET.get('item_name')
    if item_name!='' and item_name is not None:
        product_object=product_object.filter(title__icontains=item_name)
    return render(request, 'shop/index.html', {'product_object': product_object})
