from aiogram.filters import BaseFilter
from aiogram.types import Message, CallbackQuery


class IsAdmin(BaseFilter):
    '''Filter for admins'''
    def __init__(self, admin_ids: list[int]) -> None:
        self.admin_ids = admin_ids

    async def __call__(self, message: Message, callback=None | CallbackQuery) -> bool:
        if message:
            return message.from_user.id in self.admin_ids
        if callback:
            return callback.message.from_user.id in self.admin_ids


class IsPlaced(BaseFilter):
    '''Filters placed orders'''
    def __init__(self, placed_orders: list[int]) -> None:
        self.placed_orders = placed_orders

    async def __call__(self, callback: CallbackQuery) -> bool:
        return int(callback.data) in self.placed_orders


#from django.db.models.query import QuerySet
#import os
#os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'flower_shop.settings')
#os.environ['DJANGO_ALLOW_ASYNC_UNSAFE'] = 'true'
#import django
#from django.conf import settings
#
#if not settings.configured:
#    django.setup()
#
#from mainapp.models import Order


#class HasntOrders(BaseFilter):
#    '''Filters placed orders'''
#    def __init__(self) -> None:
#        self.has_orders = Order.objects.filter(status='P')
#
#    async def __call__(self, message: Message) -> bool:
#        return not bool(self.has_orders)
