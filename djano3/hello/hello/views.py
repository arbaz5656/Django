from django.http import HttpResponse
from django.shortcuts import render
def home(request):
    # return HttpResponse("shaikh Arbaz")
    return render(request,'home.html')
def login(request):
    return render(request,'login.html')