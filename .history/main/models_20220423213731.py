from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


YEAR_CHOICES = [
    ('All', 'All'),
    ('Freshman', '1'),
    ('Sophomore', '2'),
    ('Junior', '3'),
    ('Senior', '4')
]


CREDIT_CHOICES = [
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
]

DURATION_CHOICES = [
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4')
]
#User model
class User(AbstractUser):
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(unique=True, null=True)
    bio = models.TextField(null=True)
    avatar = models.ImageField(null=True, default="avatar.svg")

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

# Department model
class Topic(models.Model):
    name = models.CharField(max_length=200)
    department = models.BooleanField(default=True)

    def __str__(self):
        return self.name

#Course Room available for the students
class Room(models.Model):
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    participants = models.ManyToManyField(
        User, related_name='participants', blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.name

#message in the course room
class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    body = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated', '-created']

    def __str__(self):
        return self.body[0:50]



#model for individual courses
class Course(models.Model):
    name = models.CharField(max_length=200)
    professor = models.ForeignKey('rateMyProf.Professor', on_delete=models.CASCADE)
    year = models.CharField(max_length=100)
    courseid = models.CharField(max_length=200)
    credit = models.CharField(max_length=100, choices=CREDIT_CHOICES)
    duration = models.CharField(max_length=50, choices=DURATION_CHOICES)
    schedule = models.CharField(max_length=100)
    current_students = models.IntegerField()
    total_students = models.IntegerField()
    participants = models.ManyToManyField(User, blank=True, related_name='students', )
    major = models.ForeignKey(Topic, on_delete=models.CASCADE, blank=True)
    tag = models.CharField(max_length=200, blank=True)
    note = models.TextField(blank=True)

    def __str__(self):
        return self.name



