from django.shortcuts import render, HttpResponse
# Create your views here.

def sign_in(request) : 
     return render(request, "sign_in.html")

def sign_up(request) : 
     return render (request, "sign_up.html")