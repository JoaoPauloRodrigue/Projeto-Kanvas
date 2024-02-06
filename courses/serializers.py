from rest_framework import serializers
from .models import Course
from rest_framework.validators import UniqueValidator


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = [
            "id",
            "name",
            "status",
            "start_date",
            "end_date",
            "instructor",
            "contents",
            "students_courses",
        ]
        extra_kwargs = {
            "name": {
                "validators": [
                    UniqueValidator(
                        queryset=Course.objects.all(),
                        message="course with this name already exists.",
                    )
                ]
            },
            "contents": {"read_only": True},
            "students_courses": {"read_only": True},
        }


class CourseStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = [
            "id",
            "name",
            "students_courses",
        ]
        extra_kwargs = {
            "name": {
                "validators": [
                    UniqueValidator(
                        queryset=Course.objects.all(),
                        message="course with this name already exists.",
                    )
                ]
            },
        }
