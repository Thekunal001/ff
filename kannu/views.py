from django.shortcuts import render, HttpResponse
from datetime import datetime
from kannu.models import Contact
from django.contrib import messages

def index(request):
    return render(request, 'index.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name,email=email, phone=phone, desc=desc, date=datetime.today())
        contact.save()
        messages.success(request, 'Your message has been sent!')
    return render(request,"contact.html")

def about(request):
    return render(request,"about.html")

def BS(request):
    return render (request,"BS.html")

def LBS(request):
    return render (request,"LBS.html")

def BGT(request):
    return render (request,"BGT.html")

def MG(request):
    return render (request,"MG.html")

def MP(request):
    return render (request,"MP.html")

def RLB(request):
    return render (request,"RLB.html")

def SCB(request):
    return render (request,"SCB.html")

def SVP(request):
    return render (request,"SVP.html")