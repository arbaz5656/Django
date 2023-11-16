from django.shortcuts import render,redirect
from . models import Todoadd
# Create your views here.

def index(request):
    todo=Todoadd.objects.all()
    if request.method =='POST':
        new_todo=Todoadd(
            title=request.POST['title']  #title variable is model title variable waha se aaya hai model ki file se and ['title'] ye html page k input se ayaa hai
        )
        new_todo.save()
        return redirect('/')

    return render(request,"index.html",{'todos':todo})


def Delete(request,pk):
    todo=Todoadd.objects.get(id=pk)
    todo.delete()
    return redirect('/')
