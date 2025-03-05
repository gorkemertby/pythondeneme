from django.shortcuts import render,redirect
from django.urls import reverse
from todo.models import Exams,Quizs,Options
# Create your views here.




def AdminHub(request,user_id) : 


    exams = Exams.objects.all()
    return render(request,'admin_hub.html', {'exams':exams , 'userid':user_id})


def addQuiz(request,user_id,exam_id):
        return render(request,'addquiz.html',{"userid" : user_id , "exam_id" : exam_id})

def dbAddQuiz(request,user_id,exam_id):
            
            newqid = len(Quizs.objects.all())
            newcontent = request.POST.get('question')            
            option1 = request.POST.get('answer1')
            option2 = request.POST.get('answer2')
            option3 = request.POST.get('answer3')
            option4 = request.POST.get('answer4')
            options = [option1, option2, option3, option4]
            checked = request.POST.get('correct_answer')
            print("PRINTLIYORUM",checked)
            exam = Exams.objects.get(eid = exam_id)
            #print("PRINTLIYORUM",exam)
            newQuiz = Quizs(
                qid = newqid+2 ,
                content = newcontent,
                eid = exam,
            )
            newQuiz.save()

            for i in range(1 , 5) : 
                correctness = "false"
                if i == int(checked) : 
                      correctness = "true"                            
                else : correctness = "false"

                newOid = len(Options.objects.all())+2
                quiz = Quizs.objects.get(qid= newqid +2)
                newOption = Options(
                      oid = newOid,
                      content = options[i - 1],
                      qid = quiz,
                      correctness = correctness,
                )
                newOption.save()
                print("eklendi")


            url = reverse('addExam',args = [exam_id])
            return redirect(url)


def addExam (request,user_id):
    return render ( request , 'addexam.html' ,{'userid' : user_id})


def dbAddExam (request,user_id) : 
        #eid = request.POST.get('eid')
        content = request.POST.get('content')
        title = request.POST.get('title')
        newEid = len(Exams.objects.all())

        newExam = Exams(
            eid = newEid+2,
            content = content, 
            title = title
        )
        newExam.save()
        print("eklendiPRINTED")
        url = reverse('addExam', args=[user_id])


        return redirect(url)

