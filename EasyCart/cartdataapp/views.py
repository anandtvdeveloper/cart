from django.shortcuts import render,HttpResponse,get_object_or_404
from .models import Category,Product
from django.core.paginator import Paginator,EmptyPage,InvalidPage
# Create your views here.
def allproduct(request,c_slug=None):
    c_page = None
    p = None
    if c_slug != None:
        c_page = get_object_or_404(Category,slug=c_slug)
        p = Product.objects.filter(category=c_page, available=True)
    else:
        p = Product.objects.all().filter(available=True)


    paginator = Paginator(p, 6)
    try:
        page = int(request.GET.get('page', '1'))
    except:
        page = 1
    try:
        pp = paginator.page(page)
    except (EmptyPage, InvalidPage):
        pp = paginator.page(paginator.num_pages)



    return render(request,'category.html',{'category':c_page,'products':pp })

def acpdetail(request,c_slug,p_slug):
    try:
        product=Product.objects.get(category__slug=c_slug,slug=p_slug)
    except Exception as e:
        raise e
    return render(request,'testing.html',{'pro':product})