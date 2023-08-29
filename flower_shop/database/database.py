import os
import django
from django.conf import settings
from lexicon import LEXICON


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'flower_shop.settings')
os.environ['DJANGO_ALLOW_ASYNC_UNSAFE'] = 'true'

if not settings.configured:
    django.setup()

from mainapp.models import User


def get_delivery_man_ids() -> list[int]:
    """gets delivery man tg ids from db"""
    delivery_man = User.objects.filter(role=LEXICON['role_delivery_man'])
    delivery_man_ids = [tg_id[0] for tg_id
                        in delivery_man.values_list('tg_id')]
    return delivery_man_ids
