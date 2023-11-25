from logging import Logger

from celery.utils.log import get_task_logger

from factory import create_celery

celery = create_celery()

logger: Logger = get_task_logger(__name__)
logger.setLevel(celery.conf['LOG_LEVEL'])
