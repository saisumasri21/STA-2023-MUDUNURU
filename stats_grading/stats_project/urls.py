from django.urls import path
from . import views

urlpatterns = [
    path('', views.student_details, name='project'),
    path('project_questions/', views.project_questions, name='project_questions'),
    ]