wsgi_app = 'server:app'
bind = '0.0.0.0:8080'
workers = 1
loglevel = 'debug'
worker_class = 'gevent'
keepalive = 3

