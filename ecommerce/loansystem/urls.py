from django.urls import path 
from loansystem.views import loan_to_Shoping_cart
urlpatterns = [
 path('addingcart/<int:id>', loan_to_Shoping_cart, name='loan_to_Shoping_cart'),
 ]
