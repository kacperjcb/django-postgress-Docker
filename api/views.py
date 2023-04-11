from rest_framework.response import Response
from rest_framework.decorators import api_view
from base.models import Course, Enrollment
from .serializers import CourseSerializer, EnrollmentSerializer
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import re_path
@api_view(['GET'])
def getCourse(request):
    items = Course.objects.all()
    serializer = CourseSerializer(items, many=True)
    return Response(serializer.data)

def home(request):
    courses = Course.objects.all()
    return render(request, 'home.html', {'courses': courses})
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

@api_view(['GET'])
def getEnrollment(request):
    items = Enrollment.objects.all()
    serializer = EnrollmentSerializer(items, many=True)
    return Response(serializer.data)
@api_view(['POST'])
def addCourse(request):
    serializer= CourseSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)
@api_view(['POST'])
def addEnrollment(request):
    serializer= EnrollmentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


