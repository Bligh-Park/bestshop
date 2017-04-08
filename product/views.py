from django.shortcuts import render

# Create your views here.
def product_detail(request, product_id):
    return render(request, 'product/detail.html')