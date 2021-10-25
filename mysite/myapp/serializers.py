from .models import Course
from rest_framework import serializers

class CourseSerializer(serializers.Serializer):
    name = serializers.CharField()
    price = serializers.IntegerField()
    discount = serializers.IntegerField()
    duration = serializers.IntegerField()
    author_name = serializers.CharField()

    def create(self, validation_data):
        return Course(**validation_data)



