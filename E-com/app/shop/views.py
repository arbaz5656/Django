from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
# Create your views here.
def home1(request):
    pro=Product.Objects.all()
    print(pro)
    # parameter={}
    return render(request,'shop/home1.html')
def proser(request):
    return HttpResponse("DEtails of Product and Service:")

def media(request):
    return HttpResponse("DEtails of Media:")

def about(request):
    return HttpResponse("DEtails of About Us :")

def contact(request):
    return HttpResponse("DEtails of Contact:")

