from django.urls import path
from students.views import get_random_student, student_profiles

urlpatterns = [
    path('', get_random_student),
    path('students/', student_profiles),
]