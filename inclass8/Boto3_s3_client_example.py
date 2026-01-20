# Kotini Sai Madhuhas
# 2024.03.16
import boto3

# retrive the list of existing buckets using client
s3 = boto3.client("s3")
response = s3.list_buckets()
print(response)

# output the bucket names
for bucket in response['Buckets']:
    print(f'{bucket["Name"]}')