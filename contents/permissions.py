from rest_framework import permissions
from rest_framework.views import View, Request
from accounts.models import Account


class StudentParticipates(permissions.BasePermission):
    ...
