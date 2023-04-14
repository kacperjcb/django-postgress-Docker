from rest_framework import serializers
from base.models import Course, Enrollment

class EnrollmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enrollment
        fields = '__all__'

class CourseSerializer(serializers.ModelSerializer):
    enrollment_set = EnrollmentSerializer(many=True, read_only=True)

    class Meta:
        model = Course
        fields = '__all__'
