from django.shortcuts import render
from todo.models import  Answers, Options, User
# Create your views here.



def AnalyzeCalc() : 
    return 0



def AnalyzeView(request,user_id,exam_id):

        user = User.objects.get(id = user_id)
        print(user)
        answers = Answers.objects.filter(id = user.id)
        print(answers)    
        selected_opt_num = len(answers)




        return render(request,'analyze.html')