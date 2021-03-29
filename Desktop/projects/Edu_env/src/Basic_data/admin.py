from django.contrib import admin
from .models import Academic_year, Term, College, Nationality, Course
from Student_Stuff.models import Students, Stuff_Degrees, Stuff, User
from Lectures.models import Lecture_Duration, Lecture_Schedule
from Assessment.models import Exams, Degrees
from Departments.models import Department, Dept_Courses, College_Grades

admin.site.register(Academic_year)
admin.site.register(Term)
admin.site.register(College)
admin.site.register(Nationality)
admin.site.register(Course)
admin.site.register(Students)
admin.site.register(Stuff_Degrees)
admin.site.register(Stuff)
admin.site.register(Lecture_Duration)
admin.site.register(Lecture_Schedule)
admin.site.register(Exams)
admin.site.register(Degrees)
admin.site.register(Department)
admin.site.register(Dept_Courses)
admin.site.register(College_Grades)
admin.site.register(User)
