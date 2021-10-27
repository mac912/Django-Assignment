from django.shortcuts import render
from .models import Course
from .serializers import CourseSerializer
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
@api_view(['GET', 'POST'])
def CourseView(request):
    if request.method == 'GET':
        course = Course.objects.all()
        serializer = CourseSerializer(course, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

@api_view(['GET', 'DELETE', 'PUT'])
def CourseDetailView(request, pk):
    try:
        course = Course.objects.get(pk=pk)
    except Course.DoesNotExist:
        return Response(status=404)

    if request.method == 'DELETE':
        course.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'GET':
        serializer = CourseSerializer(course)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CourseSerializer(course, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)