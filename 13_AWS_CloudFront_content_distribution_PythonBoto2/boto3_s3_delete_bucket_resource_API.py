# Sai Madhuhas Kotini
# 2024.04.06
# delete bucket

import boto3

s3 = boto3.resource('s3')

bucket_name="kotini-cis3-ucm-boto3-test2"
s3_bucket = s3.Bucket(bucket_name)
s3_bucket.delete()

print('deleted bucket '+ bucket_name+' successfully!')