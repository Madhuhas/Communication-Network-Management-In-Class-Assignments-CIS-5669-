# Kotini Sai Madhuhas
# 2024.03.16
import boto3

# connect to s3
s3 = boto3.resource('s3')

# print bucket names
for bucket in s3.buckets.all():
    print(bucket.name)

print('\nThank you')