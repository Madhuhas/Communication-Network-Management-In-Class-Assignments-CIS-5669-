# Sai Madhuhas Kotini
# 2024.04.06
# list client

import boto3

s3 = boto3.client('s3')
buckets = s3.list_buckets()
for bucket in buckets['Buckets']:
    print("bucket name: " + bucket['Name'])

