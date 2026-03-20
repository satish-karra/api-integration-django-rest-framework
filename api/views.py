from django.shortcuts import render
from django.http import JsonResponse
from .serializers import StudentSerializer
from students.models import Student
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

# Function based views for non-PK operations
@api_view(['GET', 'POST'])
def studentView(request):
   if request.method == 'GET':
      #Get all the data form the student table
      students = Student.objects.all()
      serializer = StudentSerializer(students, many=True)
      return Response(serializer.data, status = status.HTTP_200_OK)
   elif request.method == 'POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# Getting single object PK based opertaions
@api_view(['GET','PUT', 'DELETE'])
def studentDetailView(request, pk):
    try:
        student = Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = StudentSerializer(student)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializer = StudentSerializer(student, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


   


    