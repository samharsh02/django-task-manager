from rest_framework import permissions

class IsAdminOrManager(permissions.BasePermission):
    """
    Custom permission: Only admins and managers can create/update tasks.
    Developers can only view tasks.
    """

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            if request.method in permissions.SAFE_METHODS:
                return True  # Everyone can read
            return request.user.role in ["admin", "manager"]  # Only admins & managers can modify
        return False
