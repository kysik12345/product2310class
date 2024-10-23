from django.shortcuts import render
from decimal import Decimal
from website_project.settings import CART_SESSION_ID
from app.models import Product

class Cart:
    def __int_(self, request):
        self.session = request.session
        self.user = request.user

        cart = self.session.get(CART_SESSION_ID)
        if not cart:
            cart = self.session[CART_SESSION_ID] = {}
        self.cart = cart

def save(self):
    self.session.modified = True

def add(self, product, quantity=1, override_quantity=False):
    product_id = str(product.id)
    if product_id not in self.cart:
        self.cart[product_id] = {
            'quantity': 0,
            'price':str(product.price)
        }
    if override_quantity:
        self.cart[product_id]['quantity'] = quantity
    else:
        self.cart[product_id]['quantity'] += quantity

    self.save()

def remove(self, product):
    product_id = str(product.id)
    if product_id in self.cart:
        del self.cart[product_id]
        self.save()

def __len__(self):
    return sum(item['qantity'] for item in self.cart.values())

def get_total_price(self):
    return sum(Decimal(item['price']) * item['qantity'] for item in self.cart.values())

def clear(self):
    del self.session[CART_SESSION_ID]
    self.save()

def __iter__(self):
    product_ids = self.cart.keys()
    products = Product.objects.filter(id__in=product_ids)
    cart = self.cart.copy()

    for product in products:
        cart[str(product.id)]['product'] = product

    for item in cart.values():
        item['price'] = Decimal(item['price'])
        item['total_price'] = item['price'] * item['quantity']
        yield item

def cart_add(request, product_id):
    cart = Cart(request)

    product = get_object_or_404(Product, id=product_id)
    cart.add(product=product)

    return redirect('index')

def cart_detail(request):
    cart = Cart(request)
    return render (template_name='cart/cart_detail.html', context={'cart:cart'})





