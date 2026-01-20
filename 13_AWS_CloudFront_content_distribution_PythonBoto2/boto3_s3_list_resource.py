# Sai Madhuhas Kotini
# 2024.04.06
# list buckets using resource API

import boto3

s3 = boto3.resource('s3')
#buckets = s3.list_buckets()
#for bucket in buckets['Buckets']:
#    print("bucket name: " + bucket['Name'])
for bucket in s3.buckets.all():
    print(f"{bucket.name},{bucket.creation_date}")

for s3Obj in s3.Bucket (name="kotini-cis3-ucm-boto3-test2").objects.all():
    print(s3Obj.key)
