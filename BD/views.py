

from django.shortcuts import render

# Create your views here.
from django.views import View
from django.views.generic import ListView

from .models import Product

from django.shortcuts import render
from .models import Product

def index(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})

def search(request):
    query = request.GET.get('query')
    if query:
        products = Product.objects.filter(desc__icontains=query)
    else:
        products = Product.objects.all()
    return render(request, 'index.html', {'products': products})




