#jSchool/views.py

from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from modeltest.models import Course, Student

def home(request):
    context = {
        'student_count': Student.objects.count(),
        'course_count': Course.objects.count(),
    }
    return render(request, "home.html", context)

def students(request):
    student_list =  Student.objects.all()
    paginator = Paginator(student_list, 25) # Show 25 contacts per page
    page = request.GET.get('page')
    students = paginator.get_page(page)
    context = {
        'students' : students
    }
    return render(request, "students.html", context)

def student(request, pk):
    student = get_object_or_404(Student, id=pk)
    context = {
        'student' : student,
    }
    return render(request, "student.html", context)

def courses(request):
    context = {
        'courses': Course.objects.all()
    }
    return render(request, "courses.html", context)

def course(request, pk):
    course = get_object_or_404(Course, id=pk)
    context = {
        'course' : course,
    }
    return render(request, "course.html", context)