import os

from dotenv import load_dotenv, find_dotenv


load_dotenv(find_dotenv())

access_key = os.getenv("ACCESS_KEY")
access_secret_key = os.getenv("ACCESS_SECRET_KEY")
bucket_name = os.getenv("BUCKET_NAME")
