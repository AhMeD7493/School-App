from django import forms
from .models import Exams

class ExamForm(forms.ModelForm):
    class Meta:
        model = Exams
        fields = ("year", "dept_course", "results")
        lables = {'year': '', 'course': '', 'results': ''}
