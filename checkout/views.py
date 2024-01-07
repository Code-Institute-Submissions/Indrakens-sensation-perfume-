from django.shortcuts import render, redirect, reverse 
from django.contrib import messages

from .forms import OrderForm 


def order_checkout(request):
    shopping_bag = request.session.get('bag', {}) 
    if not shopping_bag:
        messages.error(request, "Your shopping bag is empty.") 
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/order_checkout.html'  
    context = {
        'order_form': order_form, 
        'stripe_public_key': 'pk_test_51OJdpOAEPR6xmH4Zt9Hm3lStu8M6UtwfBB1bu7Tik0IBlztXkHyQnC1Dd4XYETWznzqmCbpj0qQVouHT3Gg18V2j00Q3WYEKbu',
        'client_secret': 'test client secret', 
    } 

    return render(request, template, context)     
