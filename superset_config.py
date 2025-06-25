import os
from datetime import timedelta

# Superset specific config
ROW_LIMIT = 5000
SUPERSET_WEBSERVER_PORT = int(os.environ.get('PORT', 8088))

# Flask App Builder configuration
# Your App secret key will be used for securely signing the session cookie
# and encrypting sensitive information on the database
# Make sure you are changing this key for your deployment with a strong key.
# You can generate a strong key using `openssl rand -base64 42`
SECRET_KEY = os.environ.get('SECRET_KEY', 'your-secret-key-here')

# Database configuration
# For Render, you'll typically use a managed PostgreSQL database
SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'sqlite:///superset.db')

# Redis configuration for caching
REDIS_HOST = os.environ.get('REDIS_HOST', 'localhost')
REDIS_PORT = os.environ.get('REDIS_PORT', 6379)
REDIS_CELERY_DB = os.environ.get('REDIS_CELERY_DB', 0)
REDIS_RESULTS_DB = os.environ.get('REDIS_RESULTS_DB', 1)

# Celery configuration
class CeleryConfig:
    broker_url = f"redis://{REDIS_HOST}:{REDIS_PORT}/{REDIS_CELERY_DB}"
    imports = ('superset.sql_lab', 'superset.tasks')
    result_backend = f"redis://{REDIS_HOST}:{REDIS_PORT}/{REDIS_RESULTS_DB}"
    worker_prefetch_multiplier = 1
    task_acks_late = False

CELERY_CONFIG = CeleryConfig

# Cache configuration
CACHE_CONFIG = {
    'CACHE_TYPE': 'redis',
    'CACHE_DEFAULT_TIMEOUT': 300,
    'CACHE_KEY_PREFIX': 'superset_',
    'CACHE_REDIS_HOST': REDIS_HOST,
    'CACHE_REDIS_PORT': REDIS_PORT,
    'CACHE_REDIS_DB': os.environ.get('REDIS_CACHE_DB', 2),
}

# Feature flags
FEATURE_FLAGS = {
    'DASHBOARD_NATIVE_FILTERS': True,
    'DASHBOARD_CROSS_FILTERS': True,
    'DASHBOARD_RBAC': True,
    'ENABLE_TEMPLATE_PROCESSING': True,
}

# Security settings
WTF_CSRF_ENABLED = True
WTF_CSRF_TIME_LIMIT = None
WTF_CSRF_SSL_STRICT = False

# Session configuration
PERMANENT_SESSION_LIFETIME = timedelta(days=31)
SESSION_COOKIE_HTTPONLY = True
SESSION_COOKIE_SECURE = os.environ.get('SESSION_COOKIE_SECURE', 'false').lower() == 'true'

# Logging configuration
ENABLE_TIME_ROTATE = True
TIME_ROTATE_LOG_LEVEL = 'DEBUG'
FILENAME = os.path.join(os.path.dirname(__file__), 'superset.log')

# Email configuration (optional)
# SMTP_HOST = 'your-smtp-host'
# SMTP_STARTTLS = True
# SMTP_SSL = False
# SMTP_USER = 'your-smtp-user'
# SMTP_PORT = 587
# SMTP_PASSWORD = 'your-smtp-password'
# SMTP_MAIL_FROM = 'your-email@domain.com'

# Webdriver configuration for screenshots
WEBDRIVER_BASEURL = os.environ.get('WEBDRIVER_BASEURL', 'http://localhost:8088/')
WEBDRIVER_BASEURL_USER_FRIENDLY = os.environ.get('WEBDRIVER_BASEURL_USER_FRIENDLY', 'http://localhost:8088/') 