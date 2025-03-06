from django.shortcuts import render
from todo.models import Exams,Quizs, Answers

# Create your views here.



def ExamList (request,user_id) :

        exams = Exams.objects.all()
        return render (request,"hub.html",{ "userid" : user_id ,"exams" : exams})

