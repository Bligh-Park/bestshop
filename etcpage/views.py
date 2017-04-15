from django.shortcuts import render
from product.models import Category, Product


# Create your views here.
def home(request):
    return render(request, 'etcpage/home.html', context={
        'products': Product.objects.all().order_by('-score', '-created_at')[:5]
    })