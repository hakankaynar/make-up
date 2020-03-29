import os

proc_name = "gunicorn_product"
bind = "0.0.0.0:8000"
workers = 4
accesslog = os.getenv('MU_ACCESS_LOG_FILE', '/tmp/gunicorn_access.log')
errorlog = os.getenv('MU_ERROR_LOG_FILE', '/tmp/gunicorn_error.log')