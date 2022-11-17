from rest_framework.reverse import reverse_lazy
from test_task.settings import STRIPE_SECRET_KEY

from payment.models import Item
import stripe

stripe.api_key = STRIPE_SECRET_KEY


def get_stripe_session(item_pk: int, url: str) -> stripe.checkout.Session:
    item = Item.objects.get(pk=item_pk)
    return stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[
            {
                'price_data': {
                    'currency': 'rub',
                    'unit_amount': item.price * 100,
                    'product_data': {
                        'name': item.name,
                    },
                },
                'quantity': 1,
            },
        ],
        metadata={
            "product_id": item.id
        },
        mode='payment',
        success_url=url + reverse_lazy('success'),
        cancel_url=url + reverse_lazy('cancel'),
    )
