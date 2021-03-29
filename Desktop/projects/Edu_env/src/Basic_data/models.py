from django.db import models

class Academic_year(models.Model):
    year_name = models.CharField(max_length=50)
    def __str__(self):
        return self.year_name

class Term(models.Model):
    term_name = models.CharField(max_length=50)
    def __str__(self):
        return self.term_name

class College(models.Model):
    college_name = models.CharField(max_length=50)
    def __str__(self):
        return self.college_name

class Nationality(models.Model):
    nationality_name = models.CharField(max_length=50)
    def __str__(self):
        return self.nationality_name
    
class Course(models.Model):
    course_name = models.CharField(max_length=50)
    def __str__(self):
        return self.course_name
    