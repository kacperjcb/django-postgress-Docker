from django.db import models
from django.contrib.auth.models import User

class Course(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    max_students = models.IntegerField(default=20)
    
    def __str__(self):
        return self.name

    @property
    def num_students(self):
        return Enrollment.objects.filter(course=self).count()

    @property
    def spaces_left(self):
        return self.max_students - self.num_students

class Enrollment(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return "{} enrolled in {}".format(self.user.username, self.course.name)
