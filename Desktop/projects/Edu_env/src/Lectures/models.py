from django.db import models
from datetime import time
from Basic_data.models import Course, Academic_year
from Student_Stuff.models import Stuff 
from Departments.models import Dept_Courses

class Lecture_Duration(models.Model):
    duration_name = models.CharField(max_length=20)
    start_time = models.TimeField(default=time(8))
    end_time  = models.TimeField(default=time(10))
    def __str__(self):
        return self.duration_name

class Lecture_Schedule(models.Model):
    dept_courses = models.ForeignKey(Dept_Courses, on_delete=models.CASCADE)
    year = models.ForeignKey(Academic_year, on_delete=models.CASCADE)
    duration = models.ForeignKey(Lecture_Duration, on_delete=models.CASCADE)
    stuff = models.ForeignKey(Stuff, on_delete=models.CASCADE)
    def __str__(self):
        return self.dept_courses.course.course_name
    
