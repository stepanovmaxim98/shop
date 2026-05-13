from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
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
@login_required(login_url="login")
def add_to_cart(request, pk):
    product = get_object_or_404(Product, pk=pk)
    cart, created = Cart.objects.get_or_create(user=request.user)
    item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    item.quantity += 1
    item.save()

    return redirect("cart")


# Просмотр корзины
@login_required(login_url="login")
def cart_view(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    items = cart.items.all()
    total_items = sum(item.quantity for item in items)
    total_price = sum(item.total_price() for item in items)
    return render(
        request,
        "store/cart.html",
        {
            "cart": cart,
            "items": items,
            "total_items": total_items,
            "total_price": total_price,
        },
    )


# Регистрация
def register(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        password2 = request.POST.get("password2")

        if password != password2:
            return render(request, "register.html", {"error": "Пароли не совпадают"})

        if User.objects.filter(username=username).exists():
            return render(
                request, "register.html", {"error": "Пользователь уже существует"}
            )

        user = User.objects.create_user(username=username, password=password)
        login(request, user)
        return redirect("product_list")

    return render(request, "register.html")
