# Sai Madhuhas Kotini
# 2024.04.06
# create s3 bucket using resource API

import boto3

s3 = boto3.resource('s3')
region = "us-east-2"

def createS3Bucket(bucket_name, location):
    "create a bucket"
    bucket = s3.create_bucket(
        Bucket=bucket_name, 
        CreateBucketConfiguration=location
        )
    return bucket

bucket_name = "kotini-cis3-ucm-boto3-test2"
location =  {"LocationConstraint": region}
result = createS3Bucket(bucket_name, location)
print(result)