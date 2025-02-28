from django.shortcuts import render,redirect
from django.urls import reverse
from todo.models import Exams,Quizs,Options
# Create your views here.




def AdminHub(request,user_id) : 


    exams = Exams.objects.all()
    #print("EİDPRİNTED",exams[0].eid)
    return render(request,'admin_hub.html', {'exams':exams , 'userid':user_id})


def addQuiz(request,user_id,exam_id):
        return render(request,'addquiz.html',{"userid" : user_id , "exam_id" : exam_id})

def dbAddQuiz(request,user_id,exam_id):


            
            newqid = len(Quizs.objects.all())
            newcontent = request.POST.get('question')            
            option1 = request.POST.get('question')
            option2 = request.POST.get('question')
            option3 = request.POST.get('question')
            option4 = request.POST.get('question')
            checked = request.POST.get('correct_answer')
            print(checked)
            exam = Exams.objects.get(eid = exam_id)
            print("PRINTLIYORUM",exam)
            newQuiz = Quizs(
                qid = newqid+2 ,
                content = newcontent,
                eid = exam,
            )
            newQuiz.save()

            for i in range(1 , 4) : 
                newOid = len(Options.objects.all())+2
                quiz = Quizs.objects.get(qid= newqid +2)

                newOption = Options(
                      oid = newOid,
                      content = f'option{i}',
                      qid = quiz,
                      correctness = "false",
                )
                newOption.save()


            url = reverse('addExam',args = [exam_id])
            return redirect(url)





def addExam (req,user_id,exam_id):


    return 0

