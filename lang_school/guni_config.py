command = '/home/peka97/Django-Lang-Site/.venv/bin/gunicorn'
pythonpath = '/home/peka97/Django-Lang-Site/lang_school'
bind = '127.0.0.1:8001'
workers = 3
user = 'peka97'
limit_requests_fields = '32000'
limit_requests_field_size = '0'
raw_env = 'DJANGO_SETTINGS_MODULE=lang_school.settings'