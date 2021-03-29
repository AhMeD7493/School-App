from django.shortcuts import render, redirect
from .models import Exams
from Departments.models import Dept_Courses, Department
from .forms import ExamForm

def exams(request):
    exams = Exams.objects.all()
    context = {'exams':exams}
    return render(request, 'Assessment/exams.html', context)

def create_exam(request):
    if request.method == 'POST':
        form = ExamForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('exams')
    else:
        form = ExamForm()
    context = {'form':form}
    return render(request, 'Assessment/create_exam.html', context)
 
