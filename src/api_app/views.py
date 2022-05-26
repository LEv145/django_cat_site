from __future__ import annotations

import typing as t

from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from rest_framework.response import Response
from rest_framework.parsers import JSONParser

from .serializers import UploadSerializer
from .models import Upload
from .permissions import IsOwnerOrReadOnly

if t.TYPE_CHECKING:
    from rest_framework.request import Request


@api_view(["POST", "GET"])
@permission_classes([IsOwnerOrReadOnly])
def uploads(request: Request) -> Response:
    if request.method == "GET":
        snippets = Upload.objects.all()
        serializer = UploadSerializer(snippets, many=True)
        return Response(serializer.data)

    serializer = UploadSerializer(data=request.data)
    if not serializer.is_valid():
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(["GET", "PUT", "DELETE"])
def upload_detail(request: Request, upload_id: int) -> Response:
    try:
        upload = Upload.objects.get(pk=upload_id)
    except Upload.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = UploadSerializer(upload)
        return Response(serializer.data)

    elif request.method == "PUT":
        data = JSONParser().parse(request)
        serializer = UploadSerializer(upload, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        upload.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
