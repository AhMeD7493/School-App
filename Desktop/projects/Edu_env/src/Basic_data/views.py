from django.shortcuts import render
from .models import College
from Departments.models import Department

def home(request):
    return render(request, 'Basic_data/home.html')

def colleges(request):
    colleges =  College.objects.all()
    context = {'colleges':colleges}
    return render(request, 'Basic_data/colleges.html', context)

def college(request, id):
    college = College.objects.get(pk=id)
    depts = college.department_set.all()
    context = {'college':college, 'depts':depts}
    return render(request, 'Basic_data/college.html', context)





