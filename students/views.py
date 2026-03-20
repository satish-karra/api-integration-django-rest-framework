from django.http import HttpResponse
from django.shortcuts import render


# views.students which is created in url.py(project folder)

def students(request):
    students = [
        {'id': 1, 'Name': 'satish', 'age': 26}
    ]
    return HttpResponse(students)

