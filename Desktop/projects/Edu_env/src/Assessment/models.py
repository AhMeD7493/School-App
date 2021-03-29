from django.db import models
from Basic_data.models import Academic_year, Course
from Student_Stuff.models import Students
from Departments.models import Dept_Courses


class Exams(models.Model):
    year = models.ForeignKey(Academic_year, on_delete=models.CASCADE)
    dept_course = models.ForeignKey(Dept_Courses, on_delete=models.CASCADE)
    results = models.PositiveIntegerField()
    def __str__(self):
        return self.dept_course.course.course_name
    

class Degrees(models.Model):
    student = models.ForeignKey(Students, on_delete=models.CASCADE)
    exam = models.ForeignKey(Exams, on_delete=models.CASCADE)
    degree = models.PositiveIntegerField()
    def __str__(self):
        return self.student.student_name
    