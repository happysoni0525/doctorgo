from django.shortcuts import render

def sign_up(request):
    context={}
    # if 
    return render(request,'users/sign_up.html',context)

def login(request):
    context={}
    return render(request,'users/login.html',context)
# Create your views here.
