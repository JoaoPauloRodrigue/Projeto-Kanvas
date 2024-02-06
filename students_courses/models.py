from django.db import models
from uuid import uuid4


class Student_Course_Status(models.TextChoices):
    DEFAULT = "pending"
    ACEPT = "accepted"


class StudentCourse(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True, editable=False)
    status = models.CharField(
        max_length=20,
        choices=Student_Course_Status.choices,
        default=Student_Course_Status.DEFAULT,
    )

    course = models.ForeignKey(
        "courses.Course",
        on_delete=models.CASCADE,
        related_name="students_courses",
    )

    student = models.ForeignKey(
        "accounts.Account",
        on_delete=models.CASCADE,
        related_name="students_courses",
    )
