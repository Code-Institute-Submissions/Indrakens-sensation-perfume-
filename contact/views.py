from django.shortcuts import render, redirect, reverse
from .forms import ContactForm
from django.contrib import messages
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings


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
            subject = render_to_string(
                'contact/confirmation_emails/email_subject.txt',
                )
            body = render_to_string(
                'contact/confirmation_emails/email_body.txt',
                )
        
            send_mail(
                form,
                subject,
                body,
                settings.DEFAULT_FROM_EMAIL,
            )                
            messages.success(request, 'Your message sent successfuly!')
            return redirect(reverse('home'))
        else:
            messages.error(request, 'Something went wrong, please try again.')

    else:
        form = ContactForm()

    template = 'contact/contact_us.html'
    context = {
        'form': form
    }
    return render(request, template, context)
