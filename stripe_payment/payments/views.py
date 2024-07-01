
# payments/views.py
import json
from django.shortcuts import render
import stripe
from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

stripe.api_key = settings.STRIPE_SECRET_KEY

@csrf_exempt
def create_payment_intent(request):
    try:
        data = json.loads(request.body)
        amount = data['amount']

        payment_intent = stripe.PaymentIntent.create(
            amount=amount,
            currency='inr',
        )

        return JsonResponse({
            'clientSecret': payment_intent['client_secret']
        })
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=403)

def payment_page(request):
    return render(request, 'payments/payment.html', {
        'stripe_publishable_key': settings.STRIPE_PUBLISHABLE_KEY
    })
