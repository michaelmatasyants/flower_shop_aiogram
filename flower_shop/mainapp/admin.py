from django.contrib import admin
from mainapp.models import User, Flower, Occasion, Bouqet, Order


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['tg_id', 'role']


@admin.register(Flower)
class FlowerAdmin(admin.ModelAdmin):
    list_display = ['name', 'color']


@admin.register(Occasion)
class OccasionAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Bouqet)
class BouqetAdmin(admin.ModelAdmin):
    list_display = ['price']  # Add 'Occasion', 'flowers' from m2m

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['status', 'user', 'bouqet', 'recipient_name',
                    'delivery_address', 'delivery_date', 'delivery_time']
