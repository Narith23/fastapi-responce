import os

DEBUG = os.getenv('DEBUG', False)

APP_TITLE = os.getenv('APP_TITLE', 'BASE RESPONSE')
APP_VERSION = os.getenv('APP_VERSION', '0.0.1')
APP_DESCRIPTION = os.getenv('APP_DESCRIPTION', 'API response for global use')

APP_ENV = os.getenv('APP_ENV', 'development')
DB_USERNAME = os.getenv('DB_USERNAME', 'root')
DB_PASSWORD = os.getenv('DB_PASSWORD', 'redCloud@online22')
DB_HOST = os.getenv('DB_HOST', '192.168.17.109')
DB_PORT = os.getenv('DB_PORT', 3306)
DB_NAME = os.getenv('DB_NAME', 'micromax-ticket-db')

ROUTE_PREFIX = os.getenv('ROUTE_PREFIX', 'api')
