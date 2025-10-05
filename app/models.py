from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100,primary_key=True)
    roll_number = models.CharField(max_length=20, unique=True)
    dob = models.DateField()
    email = models.EmailField(unique=True)
    department = models.CharField(max_length=100)
    interests = models.TextField(blank=True, null=True)
    submitted_at = models.DateTimeField(auto_now_add=True)

    