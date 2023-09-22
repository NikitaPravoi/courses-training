from rest_framework import serializers
from ..models import Course


# For public view
class CoursePublicSerializer(serializers.ModelSerializer):
    duration = serializers.ReadOnlyField()
    enrolled_students = serializers.ReadOnlyField()
    is_completed = serializers.ReadOnlyField()
    can_enroll = serializers.ReadOnlyField()

    class Meta:
        model = Course
        fields = ('id', 'name', 'direction', 'desc', 'num_of_lessons', 'enrolled_students',
                  'start_date', 'end_date', 'duration', 'is_completed', 'can_enroll')


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('name', 'direction', 'desc', 'num_of_lessons', 'start_date', 'end_date', 'students')


class EnrollCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ''
