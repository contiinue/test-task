from django.urls import reverse_lazy

from test_task.settings import STRIPE_SECRET_KEY

from payment.models import Item, Order
import stripe

stripe.api_key = STRIPE_SECRET_KEY


def create_payment(product_id: int, order: bool = False) -> stripe.PaymentIntent:
    """ Get custom payment """
    product = _get_instance(product_id, order)
    return stripe.PaymentIntent.create(
        amount=_get_price(product),
        currency=_get_currency(product),
        automatic_payment_methods={
            'enabled': True,
        },
    )


def get_stripe_session(product_id: int, url: str, order: bool = False) -> stripe.checkout.Session:
    """ Get session on stripe pyment page """
    product: Order | Item = _get_instance(product_id, order)
    return stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[
            {
                'price_data': {
                    'currency': _get_currency(product),
                    'unit_amount': _get_price(product),
                    'product_data': {
                        'name': product.name,
                    },
                },
                'quantity': 1,
            },
        ],
        metadata={
            "product_id": product.pk
        },
        mode='payment',
        success_url=url + reverse_lazy('success'),
        cancel_url=url + reverse_lazy('cancel'),
    )


def _get_instance(product_id: int, order: bool = False) -> Item | Order:
    """ get instance """
    return Item.objects.get(pk=product_id) if not order \
        else get_data_for_m2m_model(Order.objects.get(pk=product_id))


def _get_price(product: Item | Order) -> int:
    """ Get price. if product is Item, will get his price and return
    else get method get_discount and return price"""
    return product.price * 100 \
        if not isinstance(product, Item) else int(product.get_discount() * 100)


def _get_currency(product: Item | Order) -> str:
    """ If product id Item , will get his currency else return currency usd """
    if hasattr(product, 'currency'):
        return product.currency
    else:
        return 'usd'


def get_data_for_m2m_model(model: Order) -> Order:
    """ Getting sum of Items price this order """
    model.name = ''
    model.price = int()
    for i in model.items.all():
        model.price += i.get_discount()
        model.name += f"{i.name}, "
    return model
