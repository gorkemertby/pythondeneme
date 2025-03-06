from django.shortcuts import render
from todo.models import  Answers, Options, User, Exams, Quizs
# Create your views here.



def AnalyzeCalc() : 
    return 0



def AnalyzeView(request,user_id,exam_id):

        user = User.objects.get(id = user_id)
        exam = Exams.objects.get(eid = exam_id)
        answers = Answers.objects.filter(id = user.id,eid = exam_id)
        print(answers)
        username = user.username
        exam_name = exam.title
        selected_option = int(len(answers))
        true_rate = 0 
        #print(int(answers[0].oid))
        for i in range (0, selected_option - 1 ) :
            if Options.objects.get(oid = int(answers[i].oid.oid)).correctness == "true" : 
                 true_rate += 1 
        






        return render(request,'analyze.html',{'username' : username ,
                                              'exam_name' : exam_name ,
                                              'selected_option' : selected_option ,
                                              'true_rate' : true_rate , 
                                                })