from botocore.exceptions import ClientError
from fastapi import FastAPI, UploadFile

from config import bucket_name
from connection import get_bucket, get_resource

app = FastAPI()


@app.get("/")
async def home() -> str:
    return "This API created for Nimble company to pass my test-task. " \
           "Just visit http://127.0.0.1:8000/docs"


@app.get("/get_file")
async def get_file(key: str):
    """
    This func accepts key as a file_name, search the file in s3.bucket by the key
    and retrieve it "as is".
    Also, this func search a <file_name>.bin file by default.
    """
    s3 = get_resource()
    full_key = key + ".bin"

    try:
        content = s3.Object(bucket_name=bucket_name, key=full_key).get()["Body"].read()
        if content is None:
            return f"There is no file with following key - {key}"
        return content
    except ClientError as error:
        print(str(error))


@app.put("/add_file")
async def update_file(key: str, file: UploadFile):
    """
    This func accepts key as a file_name and a file to upload to s3.
    Also, this func creates a <file_name>.bin file by default.
    """

    content = await file.read()
    s3 = get_resource()
    bucket = get_bucket(s3)
    full_key = key + ".bin"

    try:
        bucket.put_object(
            Key=f"{full_key}",
            Body=content
        )

        return f"{full_key} was added to s3"

    except Exception as e:
        print(e, f"Enable to upload file {full_key}")
        return
