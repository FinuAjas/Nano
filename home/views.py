from categories.models import Category
from products.models import Banner, Product
from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, HttpResponseNotFound

def home(request):
    categories = Category.objects.all()
    products   = Product.objects.all()
    banners    = Banner.objects.all()
    context = {
        'categories' : categories,
        'products': products,
        'banners' : banners,
    }
    return render(request , 'home/index.html' , context)

def about_us(request):
    return render(request , 'home/about_us.html')

def contact_us(request):
    return render(request , 'home/contact_us.html')



