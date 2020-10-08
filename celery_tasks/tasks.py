from time import sleep

from celery_tasks.celery_app import app


@app.task
def do_sum(x, y) -> int:
    sleep(3)
    # Put a breakpoint inside here when testing the issue. The task will be received but never progresses.
    # Remove the breakpoint and task completes correctly.
    print('Calculating...')
    return sum([x, y])
