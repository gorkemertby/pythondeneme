from django.contrib import admin
# Register your models here.
from .models import Exams,User,Quizs,Options,Answers



admin.site.register(Exams)
admin.site.register(User)
admin.site.register(Quizs)
admin.site.register(Options)
admin.site.register(Answers)
