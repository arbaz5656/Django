#I have creatre this file-Arbaz
from django.http import HttpResponse
from django.shortcuts import render
# """Create file,read and write:"""
""""
def index(request):
     with open('one.txt','r') as f:
        # return HttpResponse(f.write("HEsllo Arbaz"))
        return HttpResponse(f.read())
"""
# """Print hello world"""
"""
def about(request):
    return HttpResponse("HELLO SHAIKH<br>Arbaz")
"""
# """Exercise 1: personal navigator"""
"""
def index(request):
    return HttpResponse('''<h3>MY persnol Navigator:</h3>
    <a href="http://127.0.0.1:8000/">Django Home</a><br>
    <a href="https://www.youtube.com/watch?v=AepgWsROO4k&list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9&index=7">Django Code With Herry</a><br>
    <a href="https://www.instagram.com/">My Instagram</a><br>
    <a href="https://www.facebook.com/">My Facebook</a><br>
    <a href="https://music.youtube.com/watch?v=vc-KxBjIbgI&list=RDAMVMFvVXaDOuaV0">My Music</a>''')
"""
# """Laying The Pipeline """
"""
def index(request):
    return HttpResponse('''<h1>Home</h1>
    <a href="http://127.0.0.1:8000/about">About</a><br>
    <a href="http://127.0.0.1:8000/notification">Notification</a><br>
    <a href="http://127.0.0.1:8000/details">Details</a><br>''')

def about(request):
    return HttpResponse('''<h1>About</h1><a href="http://127.0.0.1:8000/">Home</a>''')

def notification(request):
    return HttpResponse('''<h1>Notification</h1><a href="http://127.0.0.1:8000/">Home</a>''')

def details(request):
    return HttpResponse('''<h1>Details</h1><a href="http://127.0.0.1:8000/">Home</a>''')

"""
# """Button With anchor Tag"""
"""
def index(request):
    return HttpResponse('''<a href="https://www.youtube.com/watch?v=ta9kgf15i20&t=131s"><button class="gfg">Home</button</a>''')
"""
"""Using Templates"""
"""
def index(request):
    Dict={"Name":"Arbaz","Field":"Engineer"}
    return render(request,'first.html',Dict)
"""
"""Home page"""
"""
def index(request):
    return render(request,"first.html")
#Get the text
def about(request):
  #Analyaz the text
    var=request.GET.get('text','default')
    print(var)
    return render(request,"first.html")
"""
"""Methemetical Expretion Using GET Methods:"""
"""
def index(request):
    return render(request,'first.html')
def about(request):
    a=int(request.GET['text1'])
    b=int(request.GET['text2'])
    c=a+b
    return render(request,'Output.html',{'Result':c})
"""
"""Methemetical Expretion Using POST Methods:"""
"""
def index(request):
    return render(request,'first.html')
def about(request):
    a=int(request.POST['text1'])
    b=int(request.POST['text2'])
    c=a+b
    return render(request,'Output.html',{'Result':c})
"""
def index(request):
    return render(request,"first.html",{'wtf':'c'})