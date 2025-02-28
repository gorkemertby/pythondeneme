
from django.contrib import admin
from django.urls import path
from todo.views import sign_in, sign_up
from auth.views import AuthService, SignUpService
from exams.views import ExamList
from quiz.views import QuizView
from adminpanel.views import AdminHub,addQuiz,dbAddQuiz
from analyze.views import AnalyzeView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', sign_in) ,
    path('subscribe',sign_up) , 
    path('trySign',AuthService),
    path('addUser',SignUpService),
    path('hub/<int:user_id>/',ExamList , name = 'hub'),
    path('user/<int:user_id>/exam/<int:exam_id>/question/<int:question_id>/', QuizView, name='question_detail'),
    path('user/<int:user_id>/exam/<int:exam_id>/analyze',AnalyzeView, name='analyze'),
    path('adminuser/<int:user_id>/',AdminHub,name='addExam'),
    path('adminuser/<int:user_id>/exam/<int:exam_id>',addQuiz,name='addQuiz'),
    path('adminuser/<int:user_id>/exam/<int:exam_id>/add',dbAddQuiz,name='dbAddQuiz'),
    #path('adminuser/<int:user_id>/exam/<int:exam_id>',addExam, name = 'addExam'),
]
