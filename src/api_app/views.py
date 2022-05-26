from __future__ import annotations

import json

from django.http import HttpRequest, HttpResponse, JsonResponse

from .models import ImageStorage


def upload_image(request: HttpRequest) -> HttpResponse:
    if request.method != "POST":
        return JsonResponse(
            status=405,
            data=dict(message="HTTP method not allowed", error_info=None),
        )

    json_data = json.loads(request.body)

    try:
        file_: str = json_data["file"]
        caption: str | None = json_data.get("caption", None)
    except KeyError as error:
        return JsonResponse(
            status=400,
            data=dict(message="Bad Request", error_info=f"Invalid key: {error}"),
        )
    image = ImageStorage(file_=file_, caption=caption)
    image.save()

    return JsonResponse(
        status=201,
        data=dict(message="Created", error_info=None),
    )


