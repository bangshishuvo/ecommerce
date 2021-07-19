from django.shortcuts import render,HttpResponse,redirect
from Ecomapp.models import Setting
from Product.models import Product
# Create your views here.
def Home(request):
    setting = Setting.objects.get(id=1)
    sliding_images= Product.objects.all()
    latest_products = Product.objects.all().order_by("-id")
    products = Product.objects.all()
    context = {'setting':setting,
            'sliding_images':sliding_images,
            'latest_products':latest_products,
            'products':products  
            }
      
        #dictonary
    return render(request, 'home.html',context)


def product_single(request,id):
    setting = Setting.objects.get(id=1)
    single_product = Product.objects.get(id=id)
    
    context={
        'setting' : setting,
        'single_product':single_product
        
        

     }
    return render(request,'product-single.html',context)