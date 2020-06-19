import multiprocessing
import os

accesslog = os.getenv('GUNICORN_ACCESS_LOG', '-')
errorlog = os.getenv('GUNICORN_ERROR_LOG', '-')

if 'GUNICORN_SOCK' not in os.environ:
    bind_ip = os.getenv('GUNICORN_BIND_IP', '0.0.0.0')
    bind_port = os.getenv('GUNICORN_BIND_PORT', '80')
    bind = f'{bind_ip}:{bind_port}'
else:
    bind_sock = os.getenv('GUNICORN_SOCK')
    bind = f'unix:{bind_sock}'

reload = os.getenv('DEBUG', False)
workers = multiprocessing.cpu_count() + 1
