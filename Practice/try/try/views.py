from django.http import HttpResponse
from django.shortcuts import render
def start(request):
    return render(request,'d.html',{'D':'website'})
    # return HttpResponse("THIS IS TRY FILE:")
