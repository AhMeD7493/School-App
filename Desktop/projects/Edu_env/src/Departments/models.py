from django.db import models
from Basic_data.models import College, Term, Course

class Department(models.Model):
    college = models.ForeignKey(College, on_delete=models.CASCADE)
    dept_name = models.CharField(max_length=100)
    class Meta:
        verbose_name_plural = 'departments'
    def __str__(self):
        return self.dept_name

class College_Grades(models.Model):
    grade_name = models.CharField(max_length=100)
    def __str__(self):
        return self.grade_name

class Dept_Courses(models.Model):
    college = models.ForeignKey(College, on_delete=models.CASCADE)
    grade = models.ForeignKey(College_Grades, on_delete=models.CASCADE)
    term = models.ForeignKey(Term, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    def __str__(self):
        return self.course.course_name + '...'


    
    