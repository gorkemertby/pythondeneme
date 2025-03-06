from django.shortcuts import render, redirect, HttpResponse
from todo.models import User
from django.urls import reverse


# Create your views here.

def AuthService (request) : 
    if request.method == "POST": 
        try:
          #print(request.body)
          password = request.POST.get("password")
          email = request.POST.get("email")         
          #print("printing",email,password)
          user = User.objects.get(email=email)              
          #print(type(password) , type(user.password))
          if password == user.password :
             #print("BİLGİLER DOGRU")
             if user.role == "admin" :
                url = reverse ('addExam',args= [user.id])
                return redirect (url)
             else :  
                url = reverse('hub',args = [user.id])
                print("printed",url)
                return redirect(url)
            
          else: 
             #print("bilgiler yanlis", user.password , password)
             return redirect ("/")
        except User.DoesNotExist : 
    
         return HttpResponse("Kullanıcı Bulunamadı")
    #print("shortcut")






def SignUpService (request) : 
   if request.method == "POST": 
    try: 
      email = request.POST.get("email")
      password = request.POST.get("password")
      username = request.POST.get("username")
      name = request.POST.get("name")
      surname = request.POST.get("surname")
      grade = request.POST.get("grade")
     # print("PRINTED HEREEE",email,password,username,name,surname,grade)
      new_User = User(
            email=email,
            password=password,
            username=username,
            name=name,
            surname=surname,
            grade=grade,
            role="normal"
        )
      
      new_User.save()
      return redirect("/")
    
    except User.DoesNotExist : 
       return  HttpResponse("BASARİSİZ")

