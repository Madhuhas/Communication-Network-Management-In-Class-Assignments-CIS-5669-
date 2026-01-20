# Sai Madhuhas Kotini
# 2024.04.06
# list buckets using resource API

import boto3

s3 = boto3.resource('s3')

for bucket in s3.buckets.limit(1):
    print(f"{bucket.name},{bucket.creation_date}")

