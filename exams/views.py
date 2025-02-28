from django.shortcuts import render
from todo.models import Exams,Quizs, Answers

# Create your views here.



def ExamList (request,user_id) :

        exams = Exams.objects.all()
        exam_dict = [{'title':exams[0].title, 'content': exams[0].content , "eid" : exams[0].eid} for exam in exams]
        #print("examdict",exam_dict)

        return render (request,"hub.html",{ "userid" : user_id ,"exams" : exams})
