from django.contrib import admin

from employees.models import Employee
from .models import Student

# Register your models here.

admin.site.register(Student)
admin.site.register(Employee)