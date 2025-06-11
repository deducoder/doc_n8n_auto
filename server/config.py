from decouple import config

# HOST configuration from .env file
HOST = config('HOST',cast=str)

# PORT configuration from .env file
PORT = config('PORT', cast=int)

# DEBUG configuration from .env file
DEBUG = config('DEBUG', cast=bool)
