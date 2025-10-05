from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Student
from .serializers import StudentSerializer

@api_view(['POST'])
def apply(request):
    serializer = StudentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Application submitted successfully!"}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_applications(request):
    rollno = request.GET.get('rollno')
    department = request.GET.get('department')   
    applications = Student.objects.all().order_by('-submitted_at')  
    if rollno:
        applications = applications.filter(roll_number=rollno)
    if department:
        applications = applications.filter(department=department)  
    serializer = StudentSerializer(applications, many=True)
    return Response(serializer.data)
