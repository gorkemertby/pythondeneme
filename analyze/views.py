from django.shortcuts import render
from todo.models import User, Quizs, Exams, Answers, Options
# Create your views here.



def AnalyzeCalc() : 
    return 0



def AnalyzeView(request,user_id,exam_id):
    

    return render(request,'analyze.html')