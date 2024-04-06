from django.shortcuts import render, redirect, reverse
from .forms import ContactForm
from django.contrib import messages


def contact_us(request):
    """A view for contact form"""
    form = ContactForm()

    if not request.user.is_authenticated:
        messages.error(request, 'Login to contact us')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()       
            messages.info(request, 'Please allow up to 48 hours for us to get back to you. Thank you for contacting with us!')
            return redirect(reverse('contact_us'))
        else:
            messages.error(request, 'Something went wrong, please try again.')

    else:
        form = ContactForm()

    template = 'contact/contact_us.html'
    context = {
        'form': form
    }
    return render(request, template, context)
        