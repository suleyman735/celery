CELERY_BROKER_URL = 'redis://redis:6379/0'
CELERY_BROKER_CONNECTION_RETRY_ON_STARTUP = True
CELERY_RESULT_BACKEND = 'redis://redis:6379/0'