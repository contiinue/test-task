from django.urls import path
from .views import ItemView, CreateSession, Success, Cancel


urlpatterns = [
    path('item/<int:pk>', ItemView.as_view(), name='item'),
    path('buy/<int:pk>', CreateSession.as_view(), name='buy'),
    path('success/', Success.as_view(), name='success'),
    path('cancel/', Cancel.as_view(), name='cancel')
]
