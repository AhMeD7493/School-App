from django.db import models
from django.contrib.auth.models import AbstractUser
from Basic_data.models import Nationality, College
from Departments.models import Department, College_Grades

class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_stuff = models.BooleanField(default=False)

class Students(models.Model):
    student = models.OneToOneField(User, on_delete=models.CASCADE)
    date_of_birth = models.DateField()
    male = models.BooleanField('male', default=False)
    female = models.BooleanField('female', default=False)
    address = models.CharField(max_length=100)
    code = models.CharField(max_length=20)
    nationality = models.ForeignKey(Nationality, on_delete=models.CASCADE)
    national_id = models.CharField(max_length=20)
    college = models.ForeignKey(College, on_delete=models.CASCADE)
    dept = models.ForeignKey(Department, default=4, on_delete=models.CASCADE)
    grade = models.ForeignKey(College_Grades, on_delete=models.CASCADE)
    def __str__(self):
        return self.student.username
    


class Stuff_Degrees(models.Model):
    degree_name = models.CharField(max_length=50)
    def __str__(self):
        return self.degree_name
    
    
class Stuff(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=False)
    stuff_name = models.CharField(max_length=100)
    hire_date = models.DateField()
    salary = models.PositiveIntegerField()
    phone_number = models.CharField(max_length=20)
    male = models.BooleanField('male', default=False)
    female = models.BooleanField('female', default=False)
    college = models.ForeignKey(College, on_delete=models.CASCADE)
    address = models.CharField(max_length=100)
    degree = models.ForeignKey(Stuff_Degrees, on_delete=models.CASCADE)
    dept = models.ForeignKey(Department, default=1 , on_delete=models.CASCADE)
    def __str__(self):
        return self.stuff_name
