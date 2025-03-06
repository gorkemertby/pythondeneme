from django.shortcuts import render, redirect
from todo.models import Quizs, Options,Answers, User, Exams
from django.urls import reverse

# Create your views here.

def QuizView(request, user_id, exam_id, question_id) :     
        quizs = Quizs.objects.filter(eid = exam_id)
        
        if question_id < len(quizs) :          
                temp = "Sonraki Soru"
                #print(quizs[0].content)
                quiz_instance = Quizs.objects.get(qid=int(quizs[question_id].qid)) 
                options = Options.objects.filter(qid=quiz_instance.qid)
                exam = Exams.objects.get(eid = exam_id)
                clearAnswers(exam_id,user_id,question_id)
                #///////////////////////////////////////////////////////////////
                selected_answer = request.POST.get('selected_answer')
                if selected_answer != None :
                        newQuiz_instance =  Quizs.objects.get(qid=int(quizs[question_id - 1 ].qid)) 
                        newOptions = Options.objects.filter(qid=newQuiz_instance.qid)
                        newOid = newOptions[int(selected_answer)]
                        user = User.objects.get(id = user_id)
                        newAnswer = Answers(
                                aid = len(Answers.objects.all()) + 2 ,
                                id = user ,
                                oid = newOid,
                                content = "asdbqwd",
                                eid = exam,
                        )
                        newAnswer.save()


                
                #///////////////////////////////////////////////////////////////
                        
                #quiz_instance = Quizs.objects.get(eid = exam_id)
                #print("PRINTED",quizs, question_id)
                #print("context",quizs[question_id].content)
                if question_id == len(quizs)-1 : temp = "Sınavı Bitir"
                return render (request , 'quizs.html',{
                                                'eid' : exam_id,
                                                'quiz_content':quizs[question_id].content,
                                                "opts" : options,
                                                "qid": question_id + 1 ,
                                                "total_questions" : len(quizs),
                                                "question_number" : question_id + 1 ,
                                                "temp" : temp,
                                                "userid":user_id,},
                                                        )
        else : 
                #///////////////////////////////////////////////////////////////
                newQuiz_instance =  Quizs.objects.get(qid=int(quizs[question_id -1 ].qid)) 
                newOptions = Options.objects.filter(qid=newQuiz_instance.qid)
                selected_answer = request.POST.get('selected_answer')
                exam = Exams.objects.get(eid = exam_id)
                if selected_answer != 'null' : 
                        newOid = newOptions[int(selected_answer)]
                        user = User.objects.get(id = user_id)
                        
                        newAnswer = Answers(
                                aid = len(Answers.objects.all()) + 2 ,
                                id = user ,
                                oid = newOid,
                                content = "asdbqwd",
                                eid = exam,
                        )
                        newAnswer.save()
                #///////////////////////////////////////////////////////////////

                url = reverse('analyze', args = [user_id,exam_id])
                return redirect(url)


def clearAnswers (exam_id,user_id,question_id) :
                if question_id == 0 :
                        exam = Exams.objects.get(eid = exam_id)
                        id = User.objects.get(id = user_id) 
                        deleteList = Answers.objects.filter(eid = exam, id = id)
                        print("DELETELİST",deleteList)
                        deleteList.delete()
                        