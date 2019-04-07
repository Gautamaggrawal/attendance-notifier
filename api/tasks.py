from celery.task.schedules import crontab
from celery.decorators import periodic_task
from celery.utils.log import get_task_logger

from api.utils import *

logger = get_task_logger(__name__)


@periodic_task(
    run_every=(crontab(minute='*/1', hour='18', day_of_week='sat')),
    name="task_save_latest_student_update",
    ignore_result=True
)
def task_save_latest_student_update():
    """
    Saves latest image from Flickr
    """
    get_latest_student_attendence()
    logger.info("student attendance updated")    