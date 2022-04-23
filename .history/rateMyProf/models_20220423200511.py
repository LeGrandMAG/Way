from turtle import update
from django.db import models
from main.models import User, Course, Topic
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.


class Professor(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=100, blank=True)
    phone = models.Numb

    def __str__(self):
        return self.name



class Rating(models.Model):
    #helps keep  track of use who rate a professor
    user = models.ForeignKey(User, on_delete=models.PROTECT, default = None, related_name="user")
    professor = models.ForeignKey(Professor, on_delete=models.PROTECT, default=None, related_name="professor")
    topic = models.ForeignKey(Topic, on_delete=models.PROTECT, blank=True, default=None, related_name="topic")
    course = models.ForeignKey(Course, on_delete=models.PROTECT, default= None, related_name="course")
    comment = models.TextField(blank=True)
    created = models.DateTimeField( auto_now_add=True)
    updated = models.DateTimeField( auto_now=True)
    score = models.IntegerField(default=0,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(0),
        ]
    )
    def __str__(self):
        return str(self.course)

class finalRating(models.Model):
    professor = models.ForeignKey(Professor, on_delete=models.PROTECT, default= None, related_name= "finalRatingprof")
    course = models.ForeignKey(Course, on_delete=models.PROTECT, default=None, related_name="finalRatingUser")
    tags = models.TextField()
    attendance = models.DecimalField(decimal_places=2, max_digits=3, null=True)
    grade = models.DecimalField(decimal_places=2, max_digits=3, null=True)