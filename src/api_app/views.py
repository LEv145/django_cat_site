from __future__ import annotations

import typing as t

from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from rest_framework.response import Response

from .serializers import UploadSerializer
from .permissions import IsOwnerOrReadOnly

if t.TYPE_CHECKING:
    from rest_framework.request import Request


@api_view(["POST"])
@permission_classes([IsOwnerOrReadOnly])
def uploads(request: Request) -> Response:
    serializer = UploadSerializer(data=request.data)
    if not serializer.is_valid():
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)
