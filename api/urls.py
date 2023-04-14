from django.urls import path, include
from rest_framework import routers
from .views import CourseViewSet, CourseDetailView, EnrollmentViewSet

router = routers.DefaultRouter()
router.register('courses', CourseViewSet)
router.register('enrollments', EnrollmentViewSet)
urlpatterns = [
    path('', include(router.urls)),
    path('api/<int:pk>/', CourseDetailView.as_view(), name='course-detail'),
    path('api-auth/', include('rest_framework.urls')),
]
