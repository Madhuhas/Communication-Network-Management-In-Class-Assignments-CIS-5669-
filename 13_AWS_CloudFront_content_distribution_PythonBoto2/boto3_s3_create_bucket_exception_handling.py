# Sai Madhuhas Kotini
# 2024.04.06
# bucket exception handling

import boto3
import logging
from botocore.exceptions import ClientError
import pathlib

s3 = boto3.client('s3')
region = "us-east-2"

def uploadFile (file_name, bucket_name, object_name=None, args=None):
    "exception handling"

    if  object_name is None:
       object_name = file_name
    try:
      print('ready to upload')
      s3.upload_file(
         file_name,
         bucket_name,
         object_name,
         args
         )
    except ClientError as e:
      logging.error(e)
      return False
    
    return True

user_home=pathlib.Path(__file__).parent.resolve()
file_name='Hello.txt'
file_path=str(user_home) + '\\' + file_name
bucket_name = "kotini-cis3-ucm-boto3-test2"
result = uploadFile(file_name, bucket_name)
print (result)
