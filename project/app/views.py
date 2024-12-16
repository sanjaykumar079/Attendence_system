
from django.shortcuts import render, redirect
from .models import Student, Attendance
from .forms import AttendanceForm
from datetime import datetime

from datetime import datetime
from django.shortcuts import render, redirect
from .models import Student, Attendance
from .forms import AttendanceForm

def upload_attendance(request):
    if request.method == 'POST':
        form = AttendanceForm(request.POST)
        if form.is_valid():
            year = form.cleaned_data['year']
            branch = form.cleaned_data['branch']
            subject = form.cleaned_data['subject']
            hour = form.cleaned_data['hour']
            absentees = form.cleaned_data['absentees'].split(',')
            
            absentees_roll = [roll.strip() for roll in absentees]
            print(absentees_roll)
            students = Student.objects.filter(roll_number__in=absentees_roll)
            print(students)
            
            for student in students:
                # Determine attendance status based on whether roll number is in absentees list
                status = True if Student.roll_number in absentees else False
                Attendance.objects.update_or_create(
                    student=student,
                    date=datetime.now().date(),
                    subject=subject,
                    hour=hour,
                    defaults={'status': status}
                )
            
            return redirect('attendance_upload_success')
    else:
        form = AttendanceForm()

    return render(request, 'upload_attendance.html', {'form': form})



def view_attendance(request):
    date = request.GET.get('date')
    # subject = request.GET.get('subject')
    # hour = request.GET.get('hour')

    attendance_records = Attendance.objects.filter(date=date).select_related('student')

    return render(request, 'view_attendance.html', {
        'attendance_records': attendance_records,
        'date': date, 
        # 'subject': subject, 
        # 'hour': hour
    })

def attendance_upload_success(request):
  return render(request, 'attendance_upload_success.html')

def home(request):
  return render(request, 'home.html')

def nav(request):
  return render(request, 'nav.html')

def login(request):
  return render(request, 'login.html')

def logout(request):
  return render(request, 'logout.html')