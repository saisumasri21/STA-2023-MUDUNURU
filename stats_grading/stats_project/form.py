from django import forms
from .models import StudentDetails, ProjectQuestions, ProjectGrading


class StudentDetailsForm(forms.ModelForm):
    class Meta:
        model = StudentDetails
        fields = '__all__'


class ProjectQuestionsForm(forms.ModelForm):
    class Meta:
        model = ProjectQuestions
        fields = '__all__'


"""class ProjectGradingForm(forms.ModelForm):
    class Meta:
        model = ProjectGrading"""
