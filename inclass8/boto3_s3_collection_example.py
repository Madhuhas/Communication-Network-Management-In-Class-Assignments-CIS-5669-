#Kotini Sai Madhuhas
#2023.03.06
import boto3

# connect to s3
s3 = boto3.resource('s3')

# print bucket names
for bucket in s3.buckets.all():
    print(bucket.name)
    

for s3Obj in s3.Bucket('KotiniUCM').objects.all():
    print(s3Obj.key)