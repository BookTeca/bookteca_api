from rest_framework import permissions
from rest_framework.views import Request, View


class IsUserCollaborator(permissions.BasePermission):
    def has_permission(self, request: Request, view: View):
        return request.user.is_superuser