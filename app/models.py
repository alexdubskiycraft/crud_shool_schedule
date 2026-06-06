from django.db import models

class Subject(models.Model):
    name = models.CharField(max_length=50)

class Teacher(models.Model):
    firstname = models.CharField(max_length=150)
    lastname = models.CharField(max_length=150)
    middlename = models.CharField(max_length=150)
    subject = models.ForeignKey(Subject, related_name='subjects', on_delete=models.CASCADE) 

class Class(models.Model):
    name = models.CharField(max_length=50)

class Student(models.Model):
    firstname = models.CharField(max_length=150)
    lastname = models.CharField(max_length=150)
    middlename = models.CharField(max_length=150)
    age = models.IntegerField(max_length=2)
    classes = models.ForeignKey(Class, related_name='classes', on_delete=models.CASCADE)

class Schedule(models.Model):
    lesson_number = models.IntegerField(max_length=2)
    day_number = models.IntegerField(max_length=2)    
    subject = models.ForeignKey(Subject, related_name='subjects', on_delete=models.CASCADE)
    classes = models.ForeignKey(Class, related_name='classes', on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, related_name='teachers', on_delete=models.CASCADE)

class Grade(models.Model): 
    value = models.IntegerField(max_length=2)
    subject = models.ForeignKey(Subject, related_name='subjects', on_delete=models.CASCADE)   
    student = models.ForeignKey(Student, related_name='students', on_delete=models.CASCADE)