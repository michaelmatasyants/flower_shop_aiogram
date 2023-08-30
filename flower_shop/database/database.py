import os
import django
from django.conf import settings
from lexicon import LEXICON
from django.db.models.query import QuerySet


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'flower_shop.settings')
os.environ['DJANGO_ALLOW_ASYNC_UNSAFE'] = 'true'

if not settings.configured:
    django.setup()

from mainapp.models import User, Order


def get_delivery_man_ids() -> list[int]:
    """gets delivery man tg ids from db"""
    delivery_man = User.objects.filter(role=LEXICON['role_delivery_man'])
    delivery_man_ids = [tg_id[0] for tg_id
                        in delivery_man.values_list('tg_id')]
    return delivery_man_ids


def get_palced_orders() -> QuerySet:
    '''Returns order objects with status Placed ordered by
    delivery date and time'''
    orders = Order.objects.filter(status='P').order_by(
                '-delivery_date', '-delivery_time')
    return orders


def get_placed_order_ids(orders=get_palced_orders()) -> list[int]:
    '''Returns order objects with status Placed ordered by
    delivery date and time'''
    order_ids = [order[0] for order in orders.values_list('id')]
    return order_ids


def set_order_status(order_id: int, status: str) -> None:
    '''Changes orders status on specified status'''
    Order.objects.filter(id=order_id).update(status=status)
