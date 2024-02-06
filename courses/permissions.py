from rest_framework import permissions
from rest_framework.views import View, Request

from accounts.models import Account


class IsSuperUserAndAuthenticated(permissions.BasePermission):
    def has_permission(self, request: Request, view):
        return request.user.is_authenticated and request.user.is_superuser


class IsAuthenticated(permissions.BasePermission):
    def has_object_permission(self, request: Request, view: View) -> bool:
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_authenticated
