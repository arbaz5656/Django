from django.shortcuts import render
from django.http import HttpResponse
def Home1(request):
    return render(request,'one.html')
    # return HttpResponse("""Home page <br><br> <a href="http://127.0.0.1:8000/shop/"><button class="gfg">Shop</button></a><br><br><a href="http://127.0.0.1:8000/blog/"><button class="gfg">blog</button></a>""")

