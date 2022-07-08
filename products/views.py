from django.shortcuts import get_object_or_404, render
from categories.models import Category
from products.models import Product

 
def products(request,category_slug=None):
    category = Category.objects.all()
    categories = None
    products = None

    if category_slug != None:
        categories = get_object_or_404(Category ,slug = category_slug)
        products = Product.objects.filter(category=categories)
    else:    
        products = Product.objects.all()
    
    context = {
        'products' : products,
        'category' : category,
    }
    return render(request, "home/products.html" , context)

def product_detail(request, category_slug, product_slug):
    try:
        single_product = Product.objects.get(category__slug=category_slug, slug=product_slug)
    except Exception as e:
        raise e
    context = {
        'single_product':single_product,
    }
    return render(request, "home/product_detail.html",context)