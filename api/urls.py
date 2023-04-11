from django.urls import path 
from . import views

urlpatterns = [
    path('', views.getCourse),
    path('2/', views.getEnrollment),
    path('add/', views.addCourse),
    path('add2/', views.addEnrollment),
    path('home/', views.home),
    path('enroll/<int:course_id>/', views.enroll, name='enroll'),
    path('course/<int:pk>/', views.course_detail, name='course_detail'),
    
]