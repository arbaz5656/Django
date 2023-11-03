from django.shortcuts import render , redirect
import uuid
from .models import url
from django.http import HttpResponse
# Create your views here.

# ye normal html form k liye
def home(request):
    return render(request,"home.html")

# ye database me data save karne k liye
def create(request):
    if request.method == 'POST':
        link=request.POST['link']
        uid=str(uuid.uuid4())[:5]
        new_url=url(link=link,uuid=uid)
        new_url.save()
        return HttpResponse(uid)

def go(request,pk):
    url_details = url.objects.get(uuid=pk)
    return redirect(url_details.link)