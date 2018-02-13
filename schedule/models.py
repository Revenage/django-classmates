from django.db import models
from django.utils import timezone

DAYS_OF_WEEK = (
    (0, 'Monday'),
    (1, 'Tuesday'),
    (2, 'Wednesday'),
    (3, 'Thursday'),
    (4, 'Friday'),
    (5, 'Saturday'),
    (6, 'Sunday'),
)

EVEN_ODD = (
    ('even', 'Even'),
    ('odd', 'Odd'),
)

TIME_FORMAT = "%H:%M"

# class Pupil(models.Model):
#     name = models.CharField(max_length=30)
#     surname = models.CharField(max_length=30)
#     description = models.TextField()
#     grade = models.ForeignKey(Grade)

class Grade(models.Model):
    name = models.CharField(max_length=3)
    def __str__(self):
        return self.name

class Subject(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    def __str__(self):
        return self.name

class Teacher(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    description = models.TextField()
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    onDuty = models.BooleanField(default = True)
    def __str__(self):
        return self.name + ' '+ self.surname


class ClassRoom(models.Model):
    number = models.CharField(max_length=10)
    floor = models.PositiveSmallIntegerField()
    available = models.BooleanField(default = True)
    def __str__(self):
        return self.number

class LessonTime(models.Model):
    number = models.PositiveSmallIntegerField()
    start = models.TimeField()
    end = models.TimeField()
    def __str__(self):
        return self.start.strftime(TIME_FORMAT) + ' - ' + self.end.strftime(TIME_FORMAT)

class SheduleItem(models.Model):
    day= models.PositiveSmallIntegerField(default=0, choices=DAYS_OF_WEEK)
    even_odd= models.CharField(max_length=1, choices=EVEN_ODD, blank=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE)
    time = models.ForeignKey(LessonTime, on_delete=models.CASCADE)
    room = models.ForeignKey(ClassRoom, on_delete=models.CASCADE)

    def __str__(self):
        return DAYS_OF_WEEK[int(self.day)][1]

