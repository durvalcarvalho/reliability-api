release: python manage.py migrate

web: gunicorn reliability.wsgi --log-file -

worker: python manage.py rqworker default