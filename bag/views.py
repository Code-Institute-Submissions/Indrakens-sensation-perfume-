from django.shortcuts import (
    render, redirect, reverse, HttpResponse, get_object_or_404 
) 

from django.contrib import messages 
from products.models import Product 


def view_shopping_bag(request):
    """
    A view that renders the bag contents page 
    """

    return render(request, 'bag/shopping_bag.html')


def add_to_shopping_bag(request, item_id):
    """ 
    Add a quantity of the specified product to the shopping bag 
    """

    product = get_object_or_404(Product, pk=item_id)  
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    giftwrap = None 
    if 'product_giftwrap' in request.POST:
        giftwrap = request.POST['product_giftwrap']
    shopping_bag = request.session.get('bag', {})

    if giftwrap:
        if item_id in list(shopping_bag.keys()):
            if giftwrap in shopping_bag[item_id]['items_by_giftwrap'].keys(): 
                shopping_bag[item_id]['items_by_giftwrap'][giftwrap] += quantity
                messages.success(request, f'Updated {product.name.upper()} with included gift wrap {giftwrap.upper()} quantity to {shopping_bag[item_id]["items_by_giftwrap"][giftwrap]}') 
            else:
                shopping_bag[item_id]['items_by_giftwrap'][giftwrap] = quantity
                messages.success(request, f'Added {product.name.upper()} with included gift wrap {giftwrap.upper()} to your shopping bag') 
        else:
            shopping_bag[item_id] = {'items_by_giftwrap': {giftwrap: quantity}} 
            messages.success(request, f'Added {product.name.upper()} with included gift wrap {giftwrap.upper()} to your shopping bag')  
    else:
        if item_id in list(shopping_bag.keys()): 
            shopping_bag[item_id] += quantity
            messages.success(request, f'Updated {product.name.upper()} quantity to {shopping_bag[item_id]}')  
        else:
            shopping_bag[item_id] = quantity
            messages.success(request, f'Added {product.name.upper()} to your shopping bag') 

    request.session['bag'] = shopping_bag
    return redirect(redirect_url) 


def adjust_shopping_bag(request, item_id):
    """ 
    Adjust the quantity of the specified product to the specified amount
    """

    product = get_object_or_404(Product, pk=item_id) 
    quantity = int(request.POST.get('quantity')) 
    giftwrap = None
    if 'product_giftwrap' in request.POST:
        giftwrap = request.POST['product_giftwrap'] 
    shopping_bag = request.session.get('bag', {})

    if giftwrap:
        if quantity > 0:
            shopping_bag[item_id]['items_by_giftwrap'][giftwrap] = quantity 
            messages.success(request, f'Updated {product.name.upper()} with included gift wrap {giftwrap.upper()} quantity to {shopping_bag[item_id]["items_by_giftwrap"][giftwrap]}')  
        else: 
            del shopping_bag[item_id]['items_by_giftwrap'][giftwrap] 
            if not shopping_bag[item_id]['items_by_giftwrap']:  
                shopping_bag.pop(item_id)
            messages.success(request, f'Removed {product.name.upper()} with included gift wrap {giftwrap.upper()} from your shopping bag')          
    else:
        if quantity > 0:
            shopping_bag[item_id] = quantity
            messages.success(request, f'Updated {product.name.upper()} quantity to {shopping_bag[item_id]}') 
        else: 
            shopping_bag.pop(item_id)
            messages.success(request, f'Removed {product.name.upper()} from your shopping bag')  

    request.session['bag'] = shopping_bag
    return redirect(reverse('view_shopping_bag')) 


def remove_from_shopping_bag(request, item_id):
    """ 
    Remove the item from shopping bag
    """
    
    try:
        product = get_object_or_404(Product, pk=item_id)  
        giftwrap = None
        if 'product_giftwrap' in request.POST:
            giftwrap = request.POST['product_giftwrap'] 
        shopping_bag = request.session.get('bag', {}) 

        if giftwrap:        
            del shopping_bag[item_id]['items_by_giftwrap'][giftwrap]  
            if not shopping_bag[item_id]['items_by_giftwrap']:  
                shopping_bag.pop(item_id)
            messages.success(request, f'Removed {product.name.upper()} with included gift wrap {giftwrap.upper()} from your shopping bag')        
        else:
            shopping_bag.pop(item_id)
            messages.success(request, f'Removed {product.name.upper()} from your shopping bag')  

        request.session['bag'] = shopping_bag
        return HttpResponse(status=200)
        
    except Exception as e:
        messages.error(request, f'Error removing item: {e}') 
        return HttpResponse(status=500)     
