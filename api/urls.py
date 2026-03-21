from django.urls import path, include
from .import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('employees', views.EmployeeViewset, basename='employee')

urlpatterns = [
    path('students/', views.studentView),
    path('students/<int:pk>/', views.studentDetailView),

    # # Class based views for employees app
    # path('employees/', views.Employees.as_view()),
    # path('employees/<int:pk>/', views.EmployeeDetailView.as_view()),

    path('', include(router.urls)),

# For Nested serializers non-pk operations
    path('blogs/', views.BlogView.as_view()),
    path('comments/', views.CommentView.as_view()),

#For Nested Serializers pk based operations
    path('blogs/<int:pk>/', views.BlogDetailView.as_view()),
    path('comments/<int:pk>/', views.CommentDetailView.as_view()),


]