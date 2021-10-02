import os

APP_VERSION = "0.0.1"
APP_NAME = os.environ.get('SERVER_NAME', "ZED")
API_PREFIX = "/api"

IS_DEBUG=True