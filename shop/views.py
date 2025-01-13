from django.shortcuts import render
from django.http import HttpResponse
from math import ceil
from .models import product,contacts
# Create your views here.
def index(request):
    
    # products = product.objects.all()
    # params = {"no_of_slides":nslides,'range' : range(1,nslides),'products':products}
    # allprods = [[products, range(1,nslides), nslides],[products, range(1,nslides), nslides]]
    allprods = []
    catrpods = product.objects.values('category','id')
    cats = {item['category'] for item in catrpods}
    for cat in cats:
        prod = product.objects.filter(category=cat)
        n = len(prod)
        nslides =  n//4 + ceil((n/4)-(n//4)) 
        allprods.append([prod,range(1,nslides),nslides])
    params = {'allprods' : allprods}
    return render(request,'shop/index.html',params)


def signup(request):
    return render(request,'shop/signup.html')

def signin(request):
    return render(request,'shop/signin.html')

def contact(request):
    if request.method == 'POST':
        #print(request) for checking request
        name = request.POST.get('name','')
        email = request.POST.get('email','')
        phone = request.POST.get('phone','')
        desc = request.POST.get('desc','')
        contac = contacts(name=name,email=email,phone=phone,desc=desc)
        contac.save()
    return render(request,'shop/contact.html')

def aboutus(request):
    return render(request,'shop/aboutus.html')

def tracker(request):
    return render(request,'shop/tracker.html')

def checkout(request):
    return render(request,'shop/checkout.html')

def products(request,id):
    # fatch the product using id
    prod = product.objects.filter(id=id)
    return render(request,"shop/products.html",{'product':prod})

