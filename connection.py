import boto3

from config import (
    access_key,
    access_secret_key,
    bucket_name,
)


def get_resource():
    return boto3.resource(
        "s3",
        aws_access_key_id=access_key,
        aws_secret_access_key=access_secret_key,
    )


def get_bucket(resource):
    return resource.Bucket(bucket_name)