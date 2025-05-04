from django.db import models
from django.utils.translation import gettext_lazy as _


class TimeStamp(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class UserProfile(TimeStamp):

    name = models.CharField(max_length = 150)
    email = models.EmailField(unique = True)
    
    class Meta:
        verbose_name = _("UserProfile")
        verbose_name_plural = _("UserProfiles")

    def __str__(self):
        return self.name

class Teacher(TimeStamp):
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    expertise = models.CharField(max_length=150)
   
class Student(TimeStamp):
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    enrollment_date = models.DateField()
    
    class Meta:
        verbose_name = _("Student")
        verbose_name_plural = _("Students")

    def __str__(self):
        return self.user.name

class Category(TimeStamp):
    name = models.CharField(max_length=100)
    description = models.TextField()
    
    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")

    def __str__(self):
        return self.name


class Course(TimeStamp):
    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    students = models.ManyToManyField(Student, through='Grade')
    
    class Meta:
        verbose_name = _("Course")
        verbose_name_plural = _("Courses")

    def __str__(self):
        return self.title

class Grade(TimeStamp):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    score = models.DecimalField(max_digits=5, decimal_places=2)
    date_assigned = models.DateField(auto_now_add=True)
    
    class Meta:
        verbose_name = _("Grade")
        verbose_name_plural = _("Grades")

    def __str__(self):
        return f"{self.student.user.name} - {self.course.title} - {self.grade}"
