from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('',views.SignupPage,name='signup'),
    path('login/',views.LoginPage,name='login'),
   
    path('logout/',views.LogoutPage,name='logout'),
    
    path("index/",views.index , name="home"),
    path("contact-us/", views.contact),
    path("profile/", views.profile, name="profile"),
    path("images/",views.contact, name="img"),
    path("about/", views.about, name="aboutpage"),
    path('restaurantlist/', views.restaurant_list, name='restaurant_list'),
    path('restaurant/<int:restaurant_id>/menu/', views.menu, name='menu'),
    path('add-to-cart/<int:item_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove-from-cart/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('cart/', views.cart_view, name='cart_view'),
    path('checkout/', views.checkout, name='checkout'),
    path('restaurant/<int:restaurant_id>/order/', views.place_order, name='place_order'),
    path('order_confirmation/', views.order_confirmation, name='order_confirmation'),
    path("menu/" ,views.menu ,name="menu"),
    path("checkout_form/",views.checkout_form ,name="checkoutform"),
    path('checkoutview/', views.checkout_view, name='checkout'),
    path("order_confirmation/", views.order_confirmation)
]



