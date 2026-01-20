# Sai Madhuhas Kotini
# 2024.04.06
# list buckets using resource API

import boto3

s3 = boto3.resource('s3')

bucket_name="kotini-cis3-ucm-boto3-test2"
bucket=s3.Bucket(bucket_name)

for file in bucket.objects.filter(Prefix='Hello'):
    print(file.key)
