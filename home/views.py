from django.shortcuts import render,HttpResponse
from .models import Menu
from django.contrib.auth.models import User, auth
from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from .forms import *
from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.contrib.auth.decorators import login_required
@login_required
def profile_view(request):
    profile = request.user.profile
    return render(request, 'profile.html', {'profile': profile})
@login_required(login_url='login')
def HomePage(request):
    return render (request,'home.html')

def SignupPage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        if pass1!=pass2:
            return HttpResponse("Your password and confrom password are not Same!!")
        else:

            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('login')
    return render (request,'signup.html')

def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse ("Username or Password is incorrect!!!")

    return render (request,'login.html')

def LogoutPage(request):
    logout(request)
    return redirect('login')


def index(request):
    item = Menu.objects.all()
    context={'item':item}
    
    return render(request,"index.html", context)
def contact(request):
   
    return render(request, "contact.html" )
def profile(request):
    profile=Profile.objects.all()
    return render(request , "profile.html" ,{'profile':profile} )
def about(request):
    return render(request ,"about.html")
@login_required
def cart_view(request ):
    cart = get_object_or_404(Cart, user=request.user)
    restaurants = Restaurant.objects.all()
    return render(request, 'cart.html', { 'restaurants': restaurants, 'cart': cart})

@login_required
def add_to_cart(request, item_id):
    menu_item = get_object_or_404(MenuItem, id=item_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_item, created = CartItem.objects.get_or_create(cart=cart, menu_item=menu_item)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('cart_view')
@login_required
def remove_from_cart(request, item_id):
    cart = get_object_or_404(Cart, user=request.user)
    cart_item = get_object_or_404(CartItem, cart=cart, menu_item_id=item_id)
    cart_item.delete()
    return redirect('cart_view')

@login_required
def checkout(request):
    restaurants = Restaurant.objects.all()
    cart = get_object_or_404(Cart, user=request.user)
    if request.method == 'POST':
        restaurant_id = request.POST.get('restaurant_id')
        restaurant = get_object_or_404(Restaurant, id=restaurant_id)
        total_amount = cart.total_amount()
        order = Order.objects.create(user=request.user, restaurant=restaurant, total_amount=total_amount, status='Pending')
        for item in cart.cart_items.all():
            order.items.add(item.menu_item)
        cart.cart_items.all().delete()  # Clear cart after order
        return redirect('checkout')
    return render(request, 'checkout.html', {'restaurants': restaurants ,'cart': cart})
def restaurant_list(request):
    restaurants = Restaurant.objects.all()
    return render(request, 'restaurant_list.html', {'restaurants': restaurants})
def menu(request, restaurant_id):
    restaurant = get_object_or_404(Restaurant, id=restaurant_id)
    menu_items = MenuItem.objects.filter(restaurant=restaurant)
    menu_items = MenuItem.objects.all()
    return render(request, 'menu.html', {'restaurant': restaurant, 'menu_items': menu_items})

@login_required
def place_order(request, restaurant_id):
    restaurant = get_object_or_404(Restaurant, id=restaurant_id)
    if request.method == 'POST':
        items = request.POST.getlist('items')
        total_amount = sum(MenuItem.objects.get(id=item_id).price for item_id in items)
        order = Order.objects.create(user=request.user, restaurant=restaurant, total_amount=total_amount, status='Pending')
        order.items.set(items)
        return redirect('order_confirmation')
    return HttpResponse("Invalid request method.", status=405)
def order_confirmation(request):
    order = Order.objects.all()
    return render(request, 'order_confirmation.html', {'order': order})
def checkout_form(request):
    return render (request , "checkout_form.html")
def checkout_view(request):
    order_id=Order.objects.all()
    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("order_confirmation")  # Redirect to a success page or another view
    else:
        form = CheckoutForm()
    
    return render(request, 'checkout_form.html', {'form': form})
