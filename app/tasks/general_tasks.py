from app.tasks import celery, logger


@celery.task
def log_sub_tasks_results(results: list[bool], action: str):
    sum_success: int = sum(1 if result is True else 0 for result in results)
    logger.info(f'Finished {action} with {sum_success} successful executions out of {len(results)}')
