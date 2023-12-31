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
    }

    return render(request, template, context)     
