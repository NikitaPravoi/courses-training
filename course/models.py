from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Course(models.Model):

    class Direction(models.TextChoices):
        DESIGN = ('DESIGN', 'DESIGN')
        IT_ENGINEERING = ('IT', 'IT&ENGINEERING')
        COMPUTER_SCIENCE = ('CS', 'COMPUTER SCIENCE')
        MACHINE_LEARNING = ('ML', 'MACHINE LEARNING')
        PRODUCT = ('PM', 'PRODUCT MANAGEMENT')
        HR = ('HR', 'HUMAN RESOURCES')

    name = models.CharField(max_length=64)
    direction = models.CharField(choices=Direction.choices,
                                 default=Direction.DESIGN,
                                 max_length=256)
    desc = models.TextField()
    num_of_lessons = models.IntegerField()
    start_date = models.DateField()
    end_date = models.DateField()

    students = models.ManyToManyField(User, null=True, blank=True)

    def duration(self):
        """
        Returns course duration
        """
        return (self.end_date - self.start_date).days

    def enrolled_students(self):
        """
        Returns a num of enrolled students
        """
        return len(list(self.students.all()))

    def is_completed(self):
        """
        Checks if course is completed for today
        """
        return self.end_date < timezone.now()

    def can_enroll(self):
        """
        Проверяет, можно ли записаться на курс.
        """
        return self.end_date >= timezone.now()
