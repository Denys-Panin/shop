from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home_page'),
    path('category/<slug:category_slug>/', views.home, name='products_by_category'),
    path('about/', views.about, name='about'),
    path('contacts/', views.contacts, name='contacts'),
    path('category/<slug:category_slug>/<slug:product_slug>/', views.product, name='product_detail'),
    path('cart/', views.cart_detail, name='cart_detail'),
    path('cart/add/<int:product_id>/', views.add_cart, name='add_cart'),
    path('cart/remove/<int:product_id>/', views.cart_remove, name='cart_remove'),
    path('cart/remove_product/<int:product_id>/', views.cart_remove_product, name='cart_remove_product'),
    path('account/create/', views.sign_up_view, name='signup'),
    path('account/login/', views.login_view, name='login'),
    path('account/signout/', views.sign_out_view, name='signout'),
    path('search/', views.search, name='search'),
]
