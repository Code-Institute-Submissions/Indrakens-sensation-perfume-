from django.http import HttpResponse
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings

from .models import Order, OrderLineItem
from products.models import Product
from profiles.models import UserProfile

import json
import time
import stripe


class StripeWH_Handler:
    """Handle Stripe webhooks"""

    def __init__(self, request):
        self.request = request

    def _send_confirmation_email(self, order):
        """Send the user a confirmation email"""
        cust_email = order.user_email
        subject = render_to_string(
            'checkout/confirmation_emails/confirmation_email_subject.txt',
            {'order': order})
        body = render_to_string(
            'checkout/confirmation_emails/confirmation_email_body.txt',
            {'order': order, 'contact_email': settings.DEFAULT_FROM_EMAIL})

        send_mail(subject, body, settings.DEFAULT_FROM_EMAIL, [cust_email])

    def handle_event(self, event):
        """
        Handle a generic/unknown/unexpected webhook event
        """
        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_succeeded(self, event):
        """
        Handle the payment intent succeeded webhook from Stripe
        """
        intent = event.data.object
        pid = intent.id
        shopping_bag = intent.metadata.bag
        save_info = intent.metadata.save_info

        # Get the Charge object
        stripe_charge = stripe.Charge.retrieve(
            intent.latest_charge
        )

        billing_details = stripe_charge.billing_details
        shipping_details = intent.shipping
        grand_total = round(stripe_charge.amount / 100, 2)

        # Clean data in the shipping details
        for field, value in shipping_details.address.items():
            if value == "":
                shipping_details.address[field] = None

        # Update profile information if save_info was checked
        profile = None
        username = intent.metadata.username
        if username != 'AnonymousUser':
            profile = UserProfile.objects.get(user__username=username)
            if save_info:
                profile.profile_phone_number = shipping_details.phone
                profile.profile_country = shipping_details.address.country
                profile.profile_postcode = shipping_details.address.postal_code
                profile.profile_town_or_city = shipping_details.address.city
                profile.profile_street_address1 = shipping_details.address.line1
                profile.profile_street_address2 = shipping_details.address.line2
                profile.profile_county = shipping_details.address.state
                profile.save()

        order_exists = False
        attempt = 1
        while attempt <= 5:
            try:
                order = Order.objects.get(
                    first_name__iexact=shipping_details.name,
                    last_name__iexact=shipping_details.lastname,
                    user_email__iexact=billing_details.email,
                    user_phone_number__iexact=shipping_details.phone,
                    user_country__iexact=shipping_details.address.country,
                    user_postcode__iexact=shipping_details.address.postal_code,
                    user_town_or_city__iexact=shipping_details.address.city,
                    user_street_address1__iexact=shipping_details.address.line1,
                    user_street_address2__iexact=shipping_details.address.line2,
                    user_county__iexact=shipping_details.address.state, 
                    grand_total=grand_total,
                    original_bag=shopping_bag,
                    stripe_pid=pid,
                )
                order_exists = True
                break
            except Order.DoesNotExist:
                attempt += 1
                time.sleep(1)
        if order_exists:
            self._send_confirmation_email(order)
            return HttpResponse(
                    content=f'Webhook received: {event["type"]} | SUCCESS: Verified order already in database',
                    status=200)
        else:
            order = None
            try:
                order = Order.object.create(
                    first_name=shipping_details.name,
                    last_name=shipping_details.lastname,
                    user_profile=profile,
                    user_email=billing_details.email,
                    user_phone_number=shipping_details.phone,
                    user_country=shipping_details.address.country,
                    user_postcode=shipping_details.address.postal_code,
                    user_town_or_city=shipping_details.address.city,
                    user_street_address1=shipping_details.address.line1,
                    user_street_address2=shipping_details.address.line2,
                    user_county=shipping_details.address.state,
                    original_bag=shopping_bag,
                    stripe_pid=pid,
                )
                for item_id, item_data in json.loads(shopping_bag).items():
                    product = Product.objects.get(id=item_id)
                    if isinstance(item_data, int):
                        order_line_item = OrderLineItem(
                            order=order,
                            product=product,
                            quantity=item_data,
                        )
                        order_line_item.save()
                    else:
                        for giftwrap, quantity in item_data['items_by_giftwrap'].items():
                            order_line_item = OrderLineItem(
                                order=order,
                                product=product,
                                quantity=quantity,
                                gift_bag_size=giftwrap,
                            )
                        order_line_item.save()
            except Exception as e:
                if order:
                    order.delete()
                return HttpResponse(
                    content=f'Webhook received: {event["type"]} | ERROR: {e}',
                    status=500)
        self._send_confirmation_email(order)
        return HttpResponse(
            content=(f'Webhook received: {event["type"]} | SUCCESS: Created order in webhook'),
            status=200)

    def handle_payment_intent_payment_failed(self, event):
        """
        Handle the payment intent payment failed webhook from Stripe
        """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)
