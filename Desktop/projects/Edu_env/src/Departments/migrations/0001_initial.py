# Generated by Django 3.1.5 on 2021-01-31 15:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Basic_data', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='College_Grades',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dept_name', models.CharField(max_length=100)),
                ('college', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Basic_data.college')),
            ],
            options={
                'verbose_name_plural': 'departments',
            },
        ),
        migrations.CreateModel(
            name='Dept_Courses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('college', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Basic_data.college')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Basic_data.course')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Departments.department')),
                ('grade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Departments.college_grades')),
                ('term', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Basic_data.term')),
            ],
        ),
    ]
