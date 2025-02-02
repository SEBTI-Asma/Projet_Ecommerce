from django.urls import path, include
from store.views import index
from .views import shop_view, about_view, contact_view, blog_view, services_view , cart_view,checkout_view, search_view, details_view,cart_vieww, payment_completed_view, chambre_view, cuisine_view, salon_view
app_name = "store"

urlpatterns = [
    path("", index, name="index"),
    path("shop/", shop_view, name="shop_view"),
    path("about/", about_view, name="about_view"),
    path("contact/", contact_view, name="contact_view"),
    path("blog/", blog_view, name="blog_view"),
    path("services/", services_view, name="services_view"),
    path("cart/<pid>", cart_view, name="cart_view"),
    path("cart/", cart_vieww, name="cart_vieww"),
    path("cart-v/", cart_vieww, name="cart_v"),

    path("checkout/", checkout_view, name="checkout_view"),
    path("search/", search_view, name="search_view"),
    path("details/<pid>",details_view ,name="details_view"),
    path('paypal/', include('paypal.standard.ipn.urls')),

    path("paiement_completed/",payment_completed_view ,name="payment_completed"),
    path("chambre/",chambre_view ,name="chambre_view"),
    path("cuisine/",cuisine_view ,name="cuisine_view"),
    path("salon/",salon_view ,name="salon_view"),
]