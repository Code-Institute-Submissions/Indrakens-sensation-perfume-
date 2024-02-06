from django.shortcuts import render, redirect,  get_object_or_404 
from django.contrib import messages 
from django.contrib.auth.decorators import login_required  

from .models import UserProfile
from .forms import UserProfileForm   

from checkout.models import Order 



@login_required 
def profile(request):
       
    profile = get_object_or_404(UserProfile, user=request.user) 
    profile.save() 
    form = UserProfileForm(instance=profile) 
    orders = profile.orders.all() 
    context = {
        'profile': profile,
        'form': form,
        'orders': orders,
    }    
    template = "profiles/user_profile.html"  
    return render(request, template, context) 


@login_required
def update_profile(request, profile): 
    """ Display the user's profile. """

    profile = get_object_or_404(UserProfile, user=request.user) 

    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=profile) 
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile updated successfully') 
            return redirect('profile')  
        else:
            messages.error(request, 'Update failed.')     
    else: 
        form = UserProfileForm(instance=profile)
    orders = profile.orders.all()  
    
    template = 'profiles/update_user_profile.html'
    context = {
        'form': form,
        'orders': orders,
        'on_update_user_profile': True       
    } 

    return render(request, template, context)  


@login_required 
def user_order_history(request, order_number):
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'This is a past confirmation for order number {order_number}.'
        'A confirmation email was sent on the order date.'
    ))

    template = 'checkout/order_checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,   
    } 

    return render(request, template, context)  


@login_required 
def delete_order_history(request, order_number): 
    """ Delete order history """  
   
    order = get_object_or_404(Order, order_number=order_number) 
    if order.delete(): 
       messages.success(request, f'Order {order} deleted from order history!')
    else:
        messages.error(request, f'Deleting {order} from order history failed. Please try again.')               
 
    return redirect('profile')  
