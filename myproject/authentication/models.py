from django.urls import reverse
from datetime import timezone
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.db import models

class Course(models.Model):
    title = models.CharField(max_length=200)
    instructor = models.CharField(max_length=100)
    description = models.TextField()  # Thêm trường description
    # Các trường khác của khoá học
    def __str__(self):
        return self.title



class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = RichTextField()
    order = models.PositiveIntegerField(default=0)  # Thêm trường order để xác định thứ tự

    # Các trường khác và phương thức

    def previous_lesson(self):
        return Lesson.objects.filter(course=self.course, order__lt=self.order).last()

    def next_lesson(self):
        return Lesson.objects.filter(course=self.course, order__gt=self.order).first()

    def __str__(self):
        return self.title



# class Quiz(models.Model):
#     title = models.CharField(max_length=200)
#     start_time = models.DateTimeField()
#     end_time = models.DateTimeField()
#
#     def __str__(self):
#         return self.title

class MyModel(models.Model):
    content = RichTextField()

