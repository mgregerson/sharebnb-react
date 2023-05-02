import logging
import boto3
from botocore.exceptions import ClientError
import os


s3 = boto3.client(
  "s3",
  "us-east-1",
  aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
  aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'),
)

bucket = os.getenv('BUCKET_NAME')


def upload_file(file_name, bucket=bucket, object_name=None):
    """Upload a file to an S3 bucket

    :param file_name: File to upload
    :param bucket: Bucket to upload to
    :param object_name: S3 object name. If not specified then file_name is used
    :return: True if file was uploaded, else False
    """

    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = os.path.basename(file_name)

    # Upload the file
    s3_client = s3
    print('s3_client:', s3_client)
    try:
        response = s3_client.upload_file(file_name, bucket, object_name)
        return response
    except ClientError as e:
        logging.error(e)
        return False

def download(file_name, bucket=bucket, object_name=None ):
    """  """

    if object_name is None:
        object_name = os.path.basename(file_name)

    output = s3.download_file(bucket, object_name, file_name)
    return output

def list_all_files(bucket):
    contents = []
    for item in s3.list_objects(Bucket=bucket)['Contents']:
        contents.append(item)
    return contents