from django.contrib import admin 

from .models import Order, OrderLineItem


class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInline,)

    readonly_fields = ('order_number', 'date',
                       'user_delivery_cost', 'order_total',
                       'grand_total', 'original_bag', 
                       'stripe_pid') 
                       
    fields = ('order_number', 'user_profile', 'date', 'user_full_name',
              'user_email', 'user_phone_number', 'user_country',
              'user_postcode', 'user_town_or_city', 'user_street_address1',
              'user_street_address2', 'user_county', 'user_delivery_cost',
              'order_total', 'grand_total', 'original_bag', 
              'stripe_pid') 

    list_display = ('order_number', 'date', 'user_full_name',
                    'order_total', 'user_delivery_cost',
                    'grand_total',)   

    ordering = ('-date',) 


admin.site.register(Order, OrderAdmin)                                              
