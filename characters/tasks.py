from characters.models import Character

from celery import shared_task

from characters.scrapper import sync_characters_with_api


@shared_task
def run_sync_with_api() -> None:
    sync_characters_with_api()
