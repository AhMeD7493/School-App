# Generated by Django 3.1.5 on 2021-01-31 15:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Departments', '0001_initial'),
        ('Basic_data', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exams',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('results', models.PositiveIntegerField()),
                ('dept_course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Departments.dept_courses')),
                ('year', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Basic_data.academic_year')),
            ],
        ),
        migrations.CreateModel(
            name='Degrees',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('degree', models.PositiveIntegerField()),
                ('exam', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Assessment.exams')),
            ],
        ),
    ]