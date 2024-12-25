import requests
from celery import shared_task
from django.conf import settings
from requests import RequestException
import logging

logger = logging.getLogger(__name__)

@shared_task(
    autoretry_for=(RequestException,),
    retry_backoff=True,
    retry_kwargs={'max_retries': 5},
)
def send_telegram_message(message: str, tg_chat_id: int) -> None:
    """
    Отправка сообщения в Telegram через бот.

    :param message: Текст сообщения
    :param tg_chat_id: ID чата в Telegram
    :raises RequestException: Если отправка сообщения завершилась ошибкой
    """
    url = f"https://api.telegram.org/bot{settings.TELEGRAM_BOT_TOKEN}/sendMessage"
    data = {"chat_id": tg_chat_id, "text": message}

    try:
        response = requests.post(url, data=data, timeout=10)
        response.raise_for_status()  # Поднимает исключение для статусов >= 400
        logger.info("Сообщение успешно отправлено в чат %s", tg_chat_id)
    except RequestException as e:
        logger.error("Ошибка при отправке сообщения: %s", e)
        raise