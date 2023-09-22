from rest_framework.response import Response
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated, IsAdminUser, AllowAny
from .serializers import *
import django_filters
from django_filters.rest_framework import DjangoFilterBackend


class CourseFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    direction = django_filters.CharFilter(method='filter_by_direction')
    desc = django_filters.CharFilter(lookup_expr='icontains')
    start_date = django_filters.DateFilter(lookup_expr='gte')

    class Meta:
        model = Course
        fields = ['name', 'direction', 'desc', 'start_date']

    @staticmethod
    def filter_by_direction(queryset, name, value):
        return queryset.filter(direction__iexact=value)


# Public view of courses
class CourseListView(generics.ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CoursePublicSerializer
    permission_classes = [AllowAny]
    filter_backends = [DjangoFilterBackend]
    filterset_class = CourseFilter


# Create course
class CourseCreateAPIView(generics.CreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAdminUser, ]


# Edit course
class CourseRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAdminUser, ]


# Enroll on course
class EnrollCourseView(generics.CreateAPIView):
    serializer_class = EnrollCourseSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        course_id = request.data.get('course_id')

        try:
            course = Course.objects.get(id=course_id)
        except Course.DoesNotExist:
            return Response({'message': 'Course not found'}, status=status.HTTP_404_NOT_FOUND)

        user = request.user

        # Check if user can enroll
        if not course.can_enroll():
            return Response({'message': 'Course has already ended'}, status=status.HTTP_400_BAD_REQUEST)

        # Check if user is already assigned
        if user in course.students.all():
            return Response({'message': 'You are already assigned on that course'}, status=status.HTTP_400_BAD_REQUEST)

        # Add a user
        course.students.add(user)

        return Response({'message': 'You are successfully enrolled'}, status=status.HTTP_201_CREATED)
