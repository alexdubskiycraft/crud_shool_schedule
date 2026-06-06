from django.db import models

class Subject(models.Model):
    name = models.CharField(max_length=50)

class Teacher(models.Model):
    firstname = models.CharField(max_length=150)
    lastname = models.CharField(max_length=150)
    middlename = models.CharField(max_length=150)
    subject = models.ForeignKey(Subject, related_name='teachers', on_delete=models.CASCADE) 

class Class(models.Model):
    name = models.CharField(max_length=50)
    year = models.IntegerField()

class Student(models.Model):
    firstname = models.CharField(max_length=150)
    lastname = models.CharField(max_length=150)
    middlename = models.CharField(max_length=150)
    age = models.IntegerField()
    classes = models.ForeignKey(Class, related_name='students', on_delete=models.CASCADE)

class Schedule(models.Model):
    lesson_number = models.IntegerField()
    day_number = models.IntegerField()    
    subject = models.ForeignKey(Subject, related_name='schedules', on_delete=models.CASCADE)
    classes = models.ForeignKey(Class, related_name='schedules', on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, related_name='schedules', on_delete=models.CASCADE)

class Grade(models.Model): 
    value = models.IntegerField()
    subject = models.ForeignKey(Subject, related_name='grades', on_delete=models.CASCADE)   
    student = models.ForeignKey(Student, related_name='grades', on_delete=models.CASCADE)