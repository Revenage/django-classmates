from django.db import models

# Create your models here.


class Subject(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(blank=True)
    def __str__(self):
        return self.name

class Grade(models.Model):
    name = models.CharField(max_length=3)
    def __str__(self):
        return self.name


class Teacher(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    description = models.TextField(blank=True)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    on_duty = models.BooleanField(default = True)
    def __str__(self):
        return self.name + ' '+ self.surname

class Student(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    description = models.TextField(blank=True)
    on_duty = models.BooleanField(default = True)
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE)
    def __str__(self):
        return self.name + ' '+ self.surname

