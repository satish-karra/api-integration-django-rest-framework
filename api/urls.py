from django.urls import path
from .import views

urlpatterns = [
    path('students/', views.studentView),
    path('students/<int:pk>/', views.studentDetailView),

    # Class based views for employees app
    path('employees/', views.Employees.as_view()),
    path('employees/<int:pk>/', views.EmployeeDetailView.as_view()),
]