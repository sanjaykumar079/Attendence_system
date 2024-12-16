from django import forms
from .models import Student

class AttendanceForm(forms.Form):
    YEAR_CHOICES = [('1st-year', '1st-year'),('2nd-year','2nd-year'), ('3rd-year', '3rd-year')]
    BRANCH_CHOICES = [('AIML-A', 'AIML-A'), ('AIML-B', 'AIML-B')]
    SUBJECT_CHOICES = [('Java', 'Java'), ('DBMS', 'DBMS'), ('AI', 'AI'),('DMGT', 'DMGT'),('IC', 'IC'),('UHV', 'UHV')]
    HOUR_CHOICES = [('9:20 - 10:20','9:20 - 10:20'),('10:20 - 11:20','10:20 - 11:20'),('11:30 - 12:30','11:30 - 12:30'),('1:20 - 2:20','1:20 - 2:20'),('2:20 - 3:20','2:20 - 3:20'),('3:30 - 4:30','3:30 - 4:30')]
    
    
    
    
    year = forms.ChoiceField(choices=YEAR_CHOICES, required=True)
    branch = forms.ChoiceField(choices=BRANCH_CHOICES, required=True)
    subject = forms.ChoiceField(choices=SUBJECT_CHOICES, required=True)
    hour = forms.ChoiceField(choices=HOUR_CHOICES, required=True)
    absentees = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter roll numbers separated by commas'}))
