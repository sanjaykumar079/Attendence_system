from django.db import models

# models.py
from django.db import models

class Student(models.Model):
    roll_number = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=100)
    year = models.IntegerField()
    branch = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.roll_number}"

class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    date = models.DateField()
    subject = models.CharField(max_length=50)
    hour = models.TextField()
    status = models.BooleanField()  # 1 = Present, 0 = Absent

    class Meta:
        unique_together = ('student', 'date', 'subject', 'hour')

    def __str__(self):
        return f"{self.student.roll_number} - {self.subject} - Hour {self.hour}"
