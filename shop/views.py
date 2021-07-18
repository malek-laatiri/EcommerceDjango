from django.shortcuts import render
from requests import request

from .models import Product
from django.core.paginator import Paginator

# Create your views here.
def index(request):

    #Search code
    product_object = Product.objects.all()
    item_name=request.GET.get('item_name')
    if item_name!='' and item_name is not None:
        product_object=product_object.filter(title__icontains=item_name)

    #Paginator code
    paginator=Paginator(product_object,4)
    page=request.GET.get('page')
    product_object=paginator.get_page(page)
    return render(request, 'shop/index.html', {'product_object': product_object})


def detail(request,id):
    product=Product.objects.get(id=id)
    return  render(request,'shop/detail.html',{'product_object':product})