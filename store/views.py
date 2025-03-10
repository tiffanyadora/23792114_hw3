import random
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Product, VisualContent

def home(request):
    products = Product.get_all()
    return render(request, 'index.html', {'products': products})

def product_detail(request):
    product_id = request.GET.get('id')
    if not product_id:
        raise Http404("Product ID missing")
    
    product = Product.get_by_id(product_id)
    if not product:
        raise Http404("Product not found")
    
    visuals = VisualContent.get_for_product(product_id)

    # Get all products except the current product
    all_products = [p for p in Product.get_all() if p.product_id != product_id]

    # Randomly select 4 suggested products (or fewer if not enough exist)
    suggested_products = random.sample(all_products, min(4, len(all_products)))

    # Split features into a list (the column must exist and isn't empty)
    product_features = product.feature.split(",") if product.feature else []

    return render (request, 'store.html', {
        'product': product,
        'visuals': visuals,
        'suggested_products': suggested_products,
        'product_features': product_features,
    })

def search (request):
    query = " ".join(request.GET.get('query', '').strip().lower().split())
    
    if not query:
        return render(request, 'search.html', {'results': [], 'query': None})
    
    products = [p for p in Product.get_all() if query in " ".join(p.name.lower().split())]
    
    return render(request, 'search.html', {'results': products, 'query': query})