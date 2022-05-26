from __future__ import annotations

import typing as t

from rest_framework import permissions

from .models import Upload


if t.TYPE_CHECKING:
    from rest_framework.request import Request
    from rest_framework.views import APIView


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(
        self,
        request: Request,
        view: APIView,
        obj: t.Any,
    ) -> bool:
        if not isinstance(obj, Upload):
            return False
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user
