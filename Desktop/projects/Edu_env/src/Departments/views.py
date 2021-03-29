from django.shortcuts import render
from .models import Department, Dept_Courses

def dept(request, id):
    dept = Department.objects.get(pk=id)
    dept_courses = dept.dept_courses_set.all()
    context = {'dept':dept, 'dept_courses':dept_courses}
    return render(request, 'Departments/dept.html', context)

