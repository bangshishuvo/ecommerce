from django.urls import path 
from orderapp.views import Add_to_Shoping_cart
urlpatterns = [
 path('addingcart/<int:id>', Add_to_Shoping_cart, name='Add_to_Shoping_cart'),

]