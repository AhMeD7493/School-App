from django.urls import path, include
from .views import home, colleges, college
from Departments.views import dept
from Assessment.views import exams, create_exam

urlpatterns = [
    path('', home, name='home' ),
    path('colleges', colleges, name='colleges'),
    path('college/<int:id>', college, name='college'),
    path('dept/<int:id>', dept, name='dept'),
    path('exams', exams, name='exams'),
    path('create_exam', create_exam, name='create_exam'),
]
