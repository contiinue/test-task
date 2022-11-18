from django.urls import path
from .views import ItemView, CreateSession, CreatePayment,  Success, Cancel, OrderView

urlpatterns = [
    # main page
    path('item/<int:pk>', ItemView.as_view(), name='item'),
    path('order/<int:pk>', OrderView.as_view(), name='order'),

    # Payment
    path('buy/<int:pk>', CreateSession.as_view(), name='buy'),
    path('custom-buy/<int:pk>', CreatePayment.as_view(), name='custom-buy'),

    # Utils (info about payment)
    path('success/', Success.as_view(), name='success'),
    path('cancel/', Cancel.as_view(), name='cancel')
]
