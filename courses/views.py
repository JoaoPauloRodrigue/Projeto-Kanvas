from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from courses.models import Course
from courses.permissions import (
    IsAuthenticated,
    IsSuperUserAndAuthenticated,
)
from courses.serializers import CourseSerializer, CourseStudentSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from drf_spectacular.utils import extend_schema


class CoursesView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsSuperUserAndAuthenticated, IsAuthenticated]

    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    @extend_schema(
        operation_id="course_create",
        summary="Registro de curso",
        description="Rota para a criação do cursos.",
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

    @extend_schema(
        operation_id="courses_get",
        summary="Listagem de cursos",
        description="Rota para a listagem dos cursos.",
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class CousersDetailView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsSuperUserAndAuthenticated]

    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    @extend_schema(
        operation_id="courses_get_by_id",
        summary="Listagem de cursos por id",
        description="Rota para a busca de curso por id.",
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @extend_schema(
        operation_id="course_delete",
        summary="Deleção de cursos",
        description="Rota para a deleção do curso",
    )
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)

    @extend_schema(operation_id="course_put", exclude=True)
    def put(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class CousersDetailStudentView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsSuperUserAndAuthenticated]

    queryset = Course.objects.all()
    serializer_class = CourseStudentSerializer
