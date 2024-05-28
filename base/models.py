from django.db import models
from users.models import User

class Subject(models.Model):
    name = models.CharField(max_length=500)

    def __str__(self):
        return self.name

class Teacher(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user.full_name) 

class Class(models.Model):
    name = models.CharField(max_length=200)
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True, blank=True)
    students = models.ManyToManyField(User, related_name="students")

    def __str__(self):
        return self.name
    
class EventType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Event(models.Model):
    event_class = models.ForeignKey(Class, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    event_type = models.ForeignKey(EventType, on_delete=models.CASCADE)
    date = models.DateField()

    def __str__(self):
        return self.name

class Grade(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    grade = models.IntegerField()

    def __str__(self):
        return f"{self.user}: {self.grade} for {self.event}"
