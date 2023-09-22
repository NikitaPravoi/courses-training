from rest_framework import serializers
from ..models import Course


# For public view
class CoursePublicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('id', 'name', 'direction', 'desc', 'num_of_lessons', 'start_date', 'end_date')


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('name', 'direction', 'desc', 'num_of_lessons', 'start_date', 'end_date', 'students')


class EnrollCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ''
