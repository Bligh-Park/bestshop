from django.shortcuts import render
from product.models import Category, Product


# Create your views here.
def home(request):
    return render(request, 'etcpage/home.html', context={
        'root_categories': Category.objects.filter(parent__isnull=True).order_by('priority'),
        'products': Product.objects.all().order_by('-score', '-create_at'[:5])
    })