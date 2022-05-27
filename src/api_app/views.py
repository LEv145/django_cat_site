from __future__ import annotations

import typing as t

from django.shortcuts import get_object_or_404

from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import UploadSerializer
from .models import Upload
from .permissions import IsOwnerOrReadOnly

if t.TYPE_CHECKING:
    from rest_framework.request import Request


class UploadList(APIView):
    def get(self, _request: Request) -> Response:
        uploads = Upload.objects.all()
        serializer = UploadSerializer(uploads, many=True)
        return Response(serializer.data)

    def post(self, request: Request) -> Response:
        serializer = UploadSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class UploadDetail(APIView):
    def get(self, _request: Request, pk: int):
        upload = get_object_or_404(Upload, pk=pk)

        serializer = UploadSerializer(upload)
        return Response(serializer.data)

    def put(self, request: Request, pk: int):
        upload = get_object_or_404(Upload, pk=pk)

        serializer = UploadSerializer(upload, data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        serializer.save()
        return Response(serializer.data)

    def delete(self, request: Request, pk: int):
        upload = get_object_or_404(Upload, pk=pk)

        upload.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
