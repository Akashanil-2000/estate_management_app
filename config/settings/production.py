 
 

from os import getenv, path

from dotenv import load_dotenv

from .base import * #noqa

from .base import BASE_DIR

local_env_file = path.join(BASE_DIR, ".envs", ".env.local")

if path.isfile(local_env_file):
    load_dotenv(local_env_file)


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = getenv(
    "DJANGO_SECRET_KEY",
)

# SECURITY WARNING: don't run with debug turned on in production!
ADMIN_URL = getenv("DJANGO_ADMIN_URL")

ALLOWED_HOSTS = []

ADMINS=[
    ("Akash" , "akash.sindhuanil@gmail.com"),
]
