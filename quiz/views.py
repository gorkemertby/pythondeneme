from django.shortcuts import render, redirect
from todo.models import Quizs, Options
from django.urls import reverse

# Create your views here.

def QuizView(request, user_id, exam_id, question_id) : 
        print(user_id)
        quizs = Quizs.objects.filter(eid = exam_id)
        if question_id <= len(quizs) :
                temp = "Sonraki Soru"
                #print(quizs[0].content)
                #print("SECILI SIK ",request.POST.get('selected_answer'))
                quiz_instance = Quizs.objects.get(qid=int(question_id)) 
                options = Options.objects.filter(qid=quiz_instance) 
                print("PRINTED",options )
                if question_id == len(quizs) : temp = "Sınavı Bitir"
                return render (request , 'quizs.html',{'eid' : exam_id,
                                                'quiz_content':quizs[question_id - 1 ].content,
                                                "opts" : options,
                                                "qid": question_id + 1 ,
                                                        "total_questions" : len(quizs),
                                                        "question_number" : question_id,"temp" : temp,
                                                        "userid":user_id},
                                                        )

        else : url = reverse('analyze', args = [user_id,exam_id])
        return redirect(url)

