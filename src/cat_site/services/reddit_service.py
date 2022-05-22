from __future__ import annotations

import typing as t


if t.TYPE_CHECKING:
    from praw import Reddit


class RedditService():
    def __init__(self, reddit_client: Reddit) -> None:
        self._reddit_client = reddit_client
