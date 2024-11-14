# Generated by Django 3.2.18 on 2024-11-14 18:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('students', '0001_initial'),
        ('attendance', '0002_attendance_course'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendance',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='students.student'),
        ),
    ]