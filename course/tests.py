from django.test import TestCase
from django.core import mail
from django.utils import timezone
from datetime import timedelta
from .models import Course
from .utils import send_course_notification


class CourseNotificationTestCase(TestCase):

    def setUp(self):
        self.course = Course.objects.create(
            name="Test Course",
            desc='Easy unittests for beginners',
            direction='IT',
            num_of_lessons=17,
            start_date=timezone.now(),
            end_date=timezone.now() + timedelta(days=7),
        )

    def test_send_course_notification(self):
        # Test user
        user_email = "test@example.com"

        # Send notification
        send_course_notification(self.course, user_email)

        # Check if mail was send
        self.assertEqual(len(mail.outbox), 1)

        # Check from user email
        self.assertEqual(mail.outbox[0].from_email, "admin@example.com")

        # Check to user email
        self.assertEqual(mail.outbox[0].to, [user_email])

        # Check theme in mail
        self.assertEqual(mail.outbox[0].subject, 'Notification: Course "Test Course" starting tomorrow!')

        # Check text in mail
        self.assertIn('Dear student,', mail.outbox[0].body)
        self.assertIn('starts tomorrow', mail.outbox[0].body)


class CourseModelTestCase(TestCase):

    def setUp(self):
        self.future_course = Course.objects.create(
            name="Future Course",
            desc='Easy Java for beginners',
            direction='IT',
            num_of_lessons=17,
            start_date=timezone.now() + timedelta(days=1),
            end_date=timezone.now() + timedelta(days=10),
        )

        self.past_course = Course.objects.create(
            name="Past Course",
            desc='Learning PyTorch',
            direction='ML',
            num_of_lessons=5,
            start_date=timezone.now() - timedelta(days=10),
            end_date=timezone.now() - timedelta(days=1),
        )

    def test_can_enroll_future_course(self):
        """
        Тестирование функции can_enroll для будущего курса.
        """
        self.assertTrue(self.future_course.can_enroll())

    def test_can_enroll_past_course(self):
        """
        Тестирование функции can_enroll для прошедшего курса.
        """
        self.assertFalse(self.past_course.can_enroll())
