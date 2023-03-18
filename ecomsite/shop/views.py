from django.shortcuts import render
from .models import Product,Order
from django.core.paginator import Paginator
# Create your views here.
def index(request):
    products = Product.objects.all()
    item_name = request.GET.get('item_name')
    # search
    if item_name != '' and item_name is not None:
        products = Product.objects.filter(title__icontains = item_name)
    # paginator
    paginator = Paginator(products,4)
    current_page = request.GET.get('page')
    products = paginator.get_page(current_page)
    return render(request,'shop/index.html',{'products':products})
def details(request,id):
    products = Product.objects.get(id=id)
    return render(request,'shop/details.html',{'products':products})
def checkout(request):
    if request.method == 'POST':
        items = request.POST.get('items','')
        name = request.POST.get('name','')
        email = request.POST.get('email','')
        address = request.POST.get('address','')
        city = request.POST.get('city','')
        state = request.POST.get('state','')
        zip = request.POST.get('zip','')
        total = request.POST.get('total','')
        order = Order(items=items,name=name,email=email,address=address,city=city,state=state,zip=zip,total=total)
        order.save()
    return render(request,'shop/checkout.html')