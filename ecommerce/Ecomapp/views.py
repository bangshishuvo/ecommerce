from django.shortcuts import render,HttpResponse,redirect
from Ecomapp.models import Setting
from Product.models import Product,Category
from orderapp.models import ShopCart
# Create your views here.
def Home(request):
    current_user = request.user
    cart_product = ShopCart.objects.filter(user_id=current_user.id)
    total_amount = 0
    for p in cart_product:
        total_amount += p.product.new_price*p.quantity

    category = Category.objects.all()

    setting = Setting.objects.get(id=1)
    sliding_images= Product.objects.all()
    latest_products = Product.objects.all().order_by("-id")
    products = Product.objects.all()
    context = {'setting':setting,
            'sliding_images':sliding_images,
            'latest_products':latest_products,
            'products':products,
            'cart_product':cart_product,  
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