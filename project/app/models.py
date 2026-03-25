
from django.db import models
from django.contrib.auth.models import User

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # link to User
    phone = models.CharField(max_length=15)
    pnr = models.CharField(max_length=50, unique=True)
    department = models.CharField(max_length=50)
    semester = models.CharField(max_length=5)

    def __str__(self):
        return self.user.username
