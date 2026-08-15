from rest_framework.request import Request
from rest_framework.permissions import BasePermission, SAFE_METHODS

from user.models import User

class IsOwnerOrReadOnly(BasePermission):
    def has_object_permission(self, request: Request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        if isinstance(obj, User):
            return request.user == obj
        return request.user == obj.user