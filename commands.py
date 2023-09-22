from django.core.management.base import BaseCommand
from datetime import timedelta
from django.utils import timezone
from course.models import Course
from course.utils import send_course_notification


class Command(BaseCommand):
    help = 'Send notification that course starts tomorrow'

    def handle(self, *args, **options):
        tomorrow = timezone.now() + timedelta(days=1)
        courses = Course.objects.filter(end_date=tomorrow)

        for course in courses:
            for student in course.students.all():
                send_course_notification(course, student.email)
