# Sai Madhuhas Kotini
# 2024.04.06
# create s3 bucket using clint API

import boto3

s3 = boto3.client('s3')
region = "us-east-2"

def createS3Bucket(bucket_name, location):
    "create a bucket"
    result = s3.create_bucket(Bucket=bucket_name, CreateBucketConfiguration=location)
    return result;

bucket_name = "kotini-cis3-ucm-boto3-test1"
location =  {"LocationConstraint": region}
result = createS3Bucket(bucket_name, location)
print(result)