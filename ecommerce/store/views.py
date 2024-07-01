from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Product, CartItem, Order
# views.py

import stripe
from django.conf import settings
from django.shortcuts import render, redirect
from django.views import View
from .forms import CheckoutForm
from .models import Order

stripe.api_key = settings.STRIPE_SECRET_KEY

class CheckoutView(View):
    def get(self, request):
        form = CheckoutForm()
        return render(request, 'checkout.html', {'form': form, 'stripe_publishable_key': settings.STRIPE_PUBLISHABLE_KEY})

    def post(self, request):
        form = CheckoutForm(request.POST)
        user = request.user
        if form.is_valid():
            amount = int(form.cleaned_data['amount'] * 100)  # Convert to cents
            
            # Create Stripe PaymentIntent
            intent = stripe.PaymentIntent.create(
                amount=amount,
                currency='usd',
                receipt_email=user.email,
            )
            
            # Save order to database
            Order.objects.create(user=user, total_price=form.cleaned_data['amount'])
            
            return render(request, 'checkout.html', {'client_secret': intent['client_secret'], 'stripe_publishable_key': settings.STRIPE_PUBLISHABLE_KEY})
        return render(request, 'checkout.html', {'form': form, 'stripe_publishable_key': settings.STRIPE_PUBLISHABLE_KEY})
# Rest 

def product_list(request):
    products = Product.objects.all()
    return render(request, 'store/product_list.html', {'products': products})

@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart_item, created = CartItem.objects.get_or_create(user=request.user, product=product)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('cart_view')

@login_required
def cart_view(request):
    cart_items = CartItem.objects.filter(user=request.user)
    return render(request, 'store/cart.html', {'cart_items': cart_items})

@login_required
def checkout(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total_price = sum(item.product.price * item.quantity for item in cart_items)
    order = Order.objects.create(user=request.user, total_price=total_price)
    cart_items.delete()
    return render(request, 'store/checkout.html', {'order': order})

from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
