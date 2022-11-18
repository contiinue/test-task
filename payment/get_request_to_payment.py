from rest_framework.reverse import reverse_lazy
from test_task.settings import STRIPE_SECRET_KEY

from payment.models import Item, Order
import stripe

stripe.api_key = STRIPE_SECRET_KEY


def get_stripe_session(product_id: int, url: str, order: bool = False) -> stripe.checkout.Session:
    product = Item.objects.get(pk=product_id) if not order \
        else get_data_for_m2m_model(Order.objects.get(pk=product_id))
    return stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[
            {
                'price_data': {
                    'currency': product.currency,
                    'unit_amount': product.price * 100 if not isinstance(product,
                                                                         Item) else int(product.get_discount() * 100),
                    'product_data': {
                        'name': product.name,
                    },
                },
                'quantity': 1,
            },
        ],
        metadata={
            "product_id": product.id
        },
        mode='payment',
        success_url=url + reverse_lazy('success'),
        cancel_url=url + reverse_lazy('cancel'),
    )


def get_data_for_m2m_model(model: Order) -> Order:
    """ Getting sum of Items price this order """
    model.name = ''
    model.price = int()
    for i in model.items.all():
        model.price += i.get_discount()
        model.name += f"{i.name}, "
    return model
