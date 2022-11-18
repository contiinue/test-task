from django.http import JsonResponse
from django.views import View
from django.views.generic import DetailView, TemplateView

from test_task.settings import STRIPE_PUBLIC_KEY
from .models import Item, Order
from .get_request_to_payment import get_stripe_session, create_payment, get_data_for_m2m_model


class Success(TemplateView):
    """ If the payment is valid """
    template_name = 'payment/success.html'


class Cancel(TemplateView):
    """ If the payment is not valid """
    template_name = 'payment/cancel.html'


class CreatePayment(View):
    def post(self, request, pk):
        return JsonResponse(
            {'clientSecret': create_payment(pk, request.GET.get('order', False))['client_secret']}
        )


class CreateSession(View):
    """ Getting a page for paying for an item"""
    def post(self, request, pk):
        return JsonResponse({
            'id': get_stripe_session(pk, request.build_absolute_uri(''), request.GET.get('order', False)).id
        })


class ItemView(DetailView):
    """ Return item of primary key"""
    template_name = 'payment/payment.html'
    model = Item
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context = super(ItemView, self).get_context_data(**kwargs)
        context['STRIPE_PUBLIC_KEY'] = STRIPE_PUBLIC_KEY
        return context


class OrderView(DetailView):
    template_name = 'payment/payment.html'
    model = Order

    def get_context_data(self, **kwargs):
        context = super(OrderView, self).get_context_data(**kwargs)
        context['STRIPE_PUBLIC_KEY'] = STRIPE_PUBLIC_KEY
        context['order'] = get_data_for_m2m_model(
            context['object']
        )
        return context
