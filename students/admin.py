from django.contrib import admin

from employees.models import Employee
from students.models import Student
from blogs.models import Blog, Comment

# Register your models here.

admin.site.register(Student)
admin.site.register(Employee)

admin.site.register(Blog)
admin.site.register(Comment)