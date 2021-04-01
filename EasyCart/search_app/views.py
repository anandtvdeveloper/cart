from django.shortcuts import render

# Create your views here.
from cartdataapp.models import Product
from django.db.models import Q
def SearchResult(request):
    products=None
    query=None
    if 'q' in request.GET:
        query=request.GET.get('q')
        products = Product.objects.all().filter(Q(name__icontains=query) | Q(desc__icontains=query))
    return render(request,'search.html',{'query':query,'products':products})
