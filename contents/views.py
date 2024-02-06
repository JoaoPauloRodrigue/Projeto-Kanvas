from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from contents.models import Content
from contents.serializers import ContentSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from courses.permissions import IsSuperUserAndAuthenticated
from drf_spectacular.utils import extend_schema


class ContentView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsSuperUserAndAuthenticated]

    queryset = Content.objects.all()
    serializer_class = ContentSerializer

    def perform_create(self, serializer):
        serializer.save(course_id=self.kwargs.get("course_id"))

    @extend_schema(
        operation_id="content_create",
        summary="Criação de conteúdos e associação ao curso",
        description="Rota para a criação de conteúdo associados a um curso.",
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

    @extend_schema(operation_id="content_get_content", exclude=True)
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class ContentDetailView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsSuperUserAndAuthenticated]

    queryset = Content.objects.all()
    serializer_class = ContentSerializer

    @extend_schema(
        operation_id="content_get",
        summary="Listagem de conteúdo por id",
        description="Rota para a listagem de um único conteúdo.",
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    @extend_schema(
        operation_id="content_delete",
        summary="Deleção de conteúdo",
        description="Rota para a deleção de conteúdo",
    )
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)

    @extend_schema(operation_id="content_put", exclude=True)
    def put(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
