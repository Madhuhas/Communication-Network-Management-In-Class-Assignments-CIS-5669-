# Sai Madhuhas Kotini
# 2024.04.06
# delete bucket

import boto3

s3 = boto3.client('s3')

bucket_name="kotini-cis3-ucm-boto3-test1"

s3.delete_bucket(Bucket=bucket_name)
print('deleted bucket '+ bucket_name+' successfully!')