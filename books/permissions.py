from rest_framework import permissions

SAFE_METHODS = ('GET', 'HEAD', 'OPTIONS', 'PATCH')

class IsOwnerOrColaboratorOrReadyOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.method in SAFE_METHODS or request.user.is_superuser or obj == request.user
