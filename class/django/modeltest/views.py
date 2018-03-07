#jSchool/views.py

from django.shortcuts import render
from modeltest.models import Course, Student

def home(request):
    context = {
        'student_count': Student.objects.count(),
        'course_count': Course.objects.count(),
    }
    return render(request, "home.html", context)

def students(request):
    context = {
        'students': Student.objects
    }
    return render(request, "courses.html", context)

def courses(request):
    context = {
        'courses': Course.objects
    }
    return render(request, "courses.html", context)