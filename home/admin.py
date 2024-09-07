from django.contrib import admin
from .models import *
# from .models import Category, Product, Order, OrderItem

admin.site.register(Menu)
admin.site.register(Profile)
admin.site.register(
    [Restaurant,Cart,CartItem,Order,MenuItem ,Checkout]
)