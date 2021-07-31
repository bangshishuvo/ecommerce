from django.shortcuts import render, HttpResponse, redirect, HttpResponseRedirect, reverse
from Product.models import Category, Product

from loansystem.models import LoanCart, ShopingCartForm
# Create your views here.

# Create your views here.
def loan_to_Shoping_cart(request, id):
    url = request.META.get('HTTP_REFERER')
    current_user = request.user
    checking = LoanCart.objects.filter(
        product_id=id, user_id=current_user.id)
    if checking:
        control = 1
    else:
        control = 0

    if request.method == "POST":
        form = ShopingCartForm(request.POST)
        if form.is_valid():
            if control == 1:
                data = LoanCart.objects.filter(
                    product_id=id, user_id=current_user.id)
                data.quantity += form.cleaned_data['quantity']
                data.save()
            else:
                data = LoanCart()
                data.user_id = current_user.id
                data.product_id = id
                data.quantity = form.cleaned_data['quantity']
                data.save()
        return HttpResponseRedirect(url)        
    else:
        if control == 1:
            data = LoanCart.objects.filter(
              product_id=id, user_id=current_user.id)
            data.quantity += 1
            data.save()
        else:
            data = LoanCart()
            data.user_id = current_user.id
            data.product_id = id
            data.quantity = 1
            data.save()
        
        return HttpResponseRedirect(url)

        