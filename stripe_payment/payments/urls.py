# payments/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('create-payment-intent/', views.create_payment_intent, name='create-payment-intent'),
    path('pay/', views.payment_page, name='payment-page'),
]