from django.shortcuts import render,redirect,get_object_or_404
from ekartapp.models import Productcard
from .models import Cart,CartItem
# Create your views here.

def _cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart

def add_cart(request,product_id):
    product = Productcard.objects.get(id=product_id)
    try:
        cart = Cart.objects.get(cart_id=_cart_id)
    except Cart.DoesNotExist:
        cart = Cart.objects.create(
            cart_id = _cart_id
        )
    cart.save()

    try:
        cart_item = CartItem.objects.get(product=product,cart=cart)
        cart_item.quantity+=1
        cart_item.save()
    except CartItem.DoesNotExist:
        cart_item = CartItem.objects.create(
            product= product,
            quantity = 1,
            cart = cart,
        )
        cart_item.save()
    return redirect('cart')
def cart(request ,total=0,quantity=0,tax=0,grand_total=0, cart_items = None):
    try:
        cart = Cart.objects.get(cart_id=_cart_id)
        cart_items = CartItem.objects.filter(cart=cart)
        for cart_item in cart_items:
            total+= (cart_item.product.price * cart_item.quantity)
            quantity+= cart_item.quantity
        tax = (2*total)/100
        grand_total = total+tax
    except:
        pass
    context={
        'total':total,
        'quantity':quantity,
        'cart_items':cart_items,
        
        'grand_total':grand_total,
        'tax':tax
    }
    return render(request,'cart.html',context)

def remove_cart(request,product_id):
    cart = Cart.objects.get(cart_id=_cart_id)
    product = get_object_or_404(Productcard,id=product_id)
    cart_item = CartItem.objects.get(product=product,cart=cart)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()
    return redirect('cart')

def remove_cart_item(request,product_id):
    cart = Cart.objects.get(cart_id=_cart_id)
    product = get_object_or_404(Productcard,id=product_id)
    cart_item = CartItem.objects.get(product=product,cart=cart)
    cart_item.delete()
    return redirect('cart')