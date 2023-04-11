from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import EnrollmentForm
from .models import Course, Enrollment
from django.urls import re_path
def home(request):
    courses = Course.objects.all()
    return render(request, 'home.html', {'courses': courses})

@login_required
def enroll(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    form = EnrollmentForm(request.POST or None)
    if form.is_valid():
        enrollment = form.save(commit=False)
        enrollment.course = course
        enrollment.user = request.user
        enrollment.save()
        messages.success(request, 'You have successfully enrolled in the course!')
        return redirect('course_app:course_detail', course.id)
    return render(request, 'enroll.html', {'form': form, 'course': course})

def course_detail(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    return render(request, 'course_detail.html', {'course': course})
