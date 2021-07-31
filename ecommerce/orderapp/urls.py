from django.urls import path 
from orderapp.views import Add_to_Shoping_cart,cart_details
urlpatterns = [
 path('addingcart/<int:id>', Add_to_Shoping_cart, name='Add_to_Shoping_cart'),
 path('cart_details/',cart_details, name='cart_details'),

]