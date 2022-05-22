from .services import RedditService

from dependency_injector import containers, providers
from praw import Reddit


class Container(containers.DeclarativeContainer):
    config = providers.Configuration()

    reddit_client = providers.Factory(
        Reddit,
        user_agent="cat_site_praw_client",
    )

    reddit_service = providers.Factory(
        RedditService,
        reddit_client=reddit_client,
    )
