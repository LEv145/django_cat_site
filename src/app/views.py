from __future__ import annotations

import typing as t

from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from dependency_injector.wiring import inject, Provide


if t.TYPE_CHECKING:
    from cat_site.containers import Container
    from cat_site.services import RedditService


@inject
def index(
    request: HttpRequest,
    search_service: RedditService = Provide[Container.reddit_service],
) -> HttpResponse:
    ...
