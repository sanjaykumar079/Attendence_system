from django.contrib import admin
from .models import Student, Attendance


@admin.register(Student)
class student(admin.ModelAdmin):
    list_display = ('roll_number', 'name', 'year','branch') 
    
@admin.register(Attendance)
class Attendance(admin.ModelAdmin):
  list_display = ('student','date','subject','hour','status')
