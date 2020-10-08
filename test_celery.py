import logging
from celery_tasks.tasks import do_sum


def test_celery():
    final_sum = do_sum.delay(1, 2)
    final_sum = final_sum.get()
    logging.warning(f'Got sum {final_sum}')

if __name__ == '__main__':
    test_celery()
