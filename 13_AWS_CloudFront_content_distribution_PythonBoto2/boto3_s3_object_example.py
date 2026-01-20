# Sai Madhuhas Kotini
# 2024.04.06
# list buckets using resource API

import boto3

s3 = boto3.resource('s3')

s3Obj = s3.Object ("kotini-cis3-ucm-boto3-test2", 'Hello.txt')
print(s3Obj.content_type)
print(s3Obj.last_modified)
