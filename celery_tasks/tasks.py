from time import sleep

from celery_tasks.celery_app import app


def foo(s):
    print(f'inside foo doing some stuff: {s}')


@app.task
def do_sum(x, y) -> int:
    sleep(3)
    # Put a breakpoint inside here when testing the issue. The task will be received but never progresses.
    # Remove the breakpoint and task completes correctly.
    print('Calculating...')
    # this is for testing step-into issue. Put a breakpoint here and attempt to step-into `foo`
    foo(f'{x} + {y}')
    return sum([x, y])
