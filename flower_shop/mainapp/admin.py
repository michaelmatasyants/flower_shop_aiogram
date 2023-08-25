from django.contrib import admin
from mainapp.models import User, Flower, Occasion, Bouqet, Order


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['tg_id', 'role']


@admin.register(Flower)
class FlowerAdmin(admin.ModelAdmin):
    pass


@admin.register(Occasion)
class OccasionAdmin(admin.ModelAdmin):
    pass


@admin.register(Bouqet)
class BouqetAdmin(admin.ModelAdmin):
    pass

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    pass
