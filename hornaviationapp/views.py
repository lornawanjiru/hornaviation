from django.shortcuts import render, redirect
from django.http import HttpResponse
from  .models import Contact

# Create your views here.
def index(request):
    
    return render(request,'index.html')

def Contactus(request):
    
    return render(request,'Contactus.html')

def Services(request):
   
    return render(request,'Services.html')

def Blog(request):
    
    return render(request,'Blog.html')

def About(request):
   
    return render(request,'About.html')

def contact_info(request):
    fname = request.POST.get('fname', '')
    lname = request.POST.get('lname', '')
    email = request.POST.get('email', '')
    subject = request.POST.get('subject', '')
    message = request.POST.get('message', '')

    contacts = Contact(fname=fname, lname=lname, email=email, subject=subject, message=message)
    contacts.save()
    print ('Successful')
   
    return render(request,'Contactus.html')