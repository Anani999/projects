from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name='product_list'),
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart_view, name='cart_view'),
    # path('checkout/', views.checkout, name='checkout1'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('checkout/', views.CheckoutView.as_view(), name='checkout'),

]
