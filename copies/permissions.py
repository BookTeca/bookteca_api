from rest_framework import permissions
from rest_framework.views import Request, View


class IsUserCollaborator(permissions.BasePermission):
    def has_permission(self, request: Request, view: View):
        return request.user.is_superuser

 
class IsUserOwnerOrCollaborator(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user.is_superuser or obj == request.user