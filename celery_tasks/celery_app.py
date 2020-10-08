from celery import Celery

app = Celery('celery_tasks',
             broker='amqp://localhost:5672',
             backend='amqp://localhost:5672',
             include=['celery_tasks.tasks'])

if __name__ == '__main__':
    app.start()
