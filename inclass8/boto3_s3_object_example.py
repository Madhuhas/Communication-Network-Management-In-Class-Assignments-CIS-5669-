#Kotini Sai Madhuhas

import boto3

# connect to s3
s3 = boto3.resource('s3')
s3Obj = s3.Object('KotiniUCM', 'HelloDolly.txt')

print(s3Obj.content_type)
print(s3Obj.last_modified)