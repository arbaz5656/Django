from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User,auth
import requests
from bs4 import BeautifulSoup

# Registration page defination.
def register(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        confirmpassword=request.POST['confirmpassword']

#Condition for not match password and confirm password.
        if password==confirmpassword:
            #Condition for alredy used username return not use.
            if User.objects.filter(username=username).exists():
                messages.info(request,"Invalid! Choos different Username.Because is already used:")
                return redirect('http://127.0.0.1:8000/')
            # Condition for alredy used email return not use.
            elif User.objects.filter(email=email).exists():
                messages.info(request, "Invalid! Email is already used.")
                return redirect('http://127.0.0.1:8000/')
            # User created defination and connect to the database.
            else:
                user=User.objects.create_user(username=username,password=password,email=email,first_name=first_name,last_name=last_name)
                user.save()
                print("User Succsefully created")
                return redirect("http://127.0.0.1:8000/login")
        else:
            print("Password not match")
            messages.info(request, "Password doesn't match!")
            return redirect('http://127.0.0.1:8000/')
    else:
        return render(request,'R.html')



# login page defination.
def login(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        # check the username and password are matching the database.
        user=auth.authenticate(username=username,password=password)
        # User succssefully login.
        if user is not None:
            auth.login(request,user)
            return redirect("http://127.0.0.1:8000/home")
        else:
            # Else
            messages.info(request,"Invalid Username & Password")
            return redirect("http://127.0.0.1:8000/login")
    else:
        return render(request,"L.html")

# home page defination
def home(request):
    return render(request,"Home.html")


# Logout
def logout(request):
    auth.logout(request)
    return redirect("http://127.0.0.1:8000/login")

# News
def news(request):
    url_link = "https://timesofindia.indiatimes.com/"
    v1 = requests.get(url_link)
    v2 = v1.content
    v3 = BeautifulSoup(v2, 'html.parser')

    v4 = v3.find_all('p')
    v5 = v3.find_all('h1')
    v6 = v3.find_all('h2')
    v7 = v3.find_all('h3')
    v8 = v3.find_all('h4')
    v9 = v3.find_all('h5')
    v10 = v3.find_all('h6')
    context = {
        "data": [v4],
        "data1": [v5],
        "datab": [v6],
        "data3": [v7],
        "data4": [v8],
        "data5": [v9],
        "data6": [v10],
    }
    return render(request,"news.html",context)