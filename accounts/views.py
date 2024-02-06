from accounts.models import Account
from rest_framework.generics import CreateAPIView
from accounts.serializers import AccountSerializer
from drf_spectacular.utils import extend_schema


class AccountView(CreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

    @extend_schema(
        operation_id="user_create",
        summary="Registro de conta",
        description="Rota para a criação da conta de usuário",
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
