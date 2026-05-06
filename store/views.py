from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Cart, CartItem


# все товары магазина
def product_list(request):
    products = Product.objects.all()
    return render(request, "store/product_list.html", {"products": products})


# Детальная информация про товар
def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, "store/product_detail.html", {"product": product})


# Добавить в корзину
def add_to_cart(request, pk):
    product = get_object_or_404(Product, pk)
    cart, created = Cart.objects.get_or_creat(user=request.user)
    item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    item.quantity += 1
    item.save()

    return redirect("cart")


# Просмотр корзирны
def cart_view(request):
    cart, created = Cart.objects.get_or_creat(user=request.user)
    items = cart.items.all()
    total_items = sum(item.quantity for item in items)
    return render(
        request,
        "store/cart.html",
        {"cart": cart, "items": items, "total_items": total_items},
    )
