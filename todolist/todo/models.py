from django.db import models

# Create your models here.

class User(models.Model) : 
    password = models.CharField(max_length= 20)
    email = models.CharField( max_length= 35) 
    username = models.CharField(max_length= 20)
    name = models.CharField(max_length= 20)
    surname = models.CharField(max_length= 20)
    grade = models.IntegerField(10)
    gender = models.CharField(max_length= 20)
    role = models.CharField(max_length= 20)

class Exams (models.Model) : 
    eid = models.BigIntegerField(primary_key=True)
    content = models.CharField(max_length=50)
    title = models.CharField(max_length=20)

class Quizs (models.Model) :  
    qid = models.BigIntegerField(primary_key=True)
    eid = models.ForeignKey(Exams,on_delete=models.CASCADE)
    content = models.CharField(max_length=50)   

class Options (models.Model) : 
    oid = models.BigIntegerField(primary_key = True)
    qid = models.ForeignKey(Quizs,on_delete=models.CASCADE)
    content = models.CharField(max_length=50)
    correctness = models.CharField(max_length=20)

class Answers (models.Model) : 
    aid = models.BigIntegerField(primary_key = True)
    id = models.ForeignKey(User,on_delete=models.CASCADE)
    oid = models.ForeignKey(Options,on_delete=models.CASCADE)
    content = models.CharField(max_length=50)
    eid = models.ForeignKey(Exams,on_delete=models.CASCADE)

class AnalyzeModel (models.Model) : 
    analyze_id = models.BigIntegerField(primary_key=True)
    id = models.ForeignKey(User,on_delete=models.CASCADE)
    eid = models.ForeignKey(Exams,on_delete=models.CASCADE)
    qid = models.ForeignKey(Quizs,on_delete=models.CASCADE)
    oid = models.ForeignKey(Options,on_delete=models.CASCADE)
    aid = models.ForeignKey(Answers,on_delete=models.CASCADE)

