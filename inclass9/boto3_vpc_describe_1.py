# Kotini Sai Madhuhas
print ('Kotini Sai Madhuhas boto3 vpc describe')

import boto3

client = boto3.client('ec2')

# copy the vpc id from the console
response = client.describe_vpcs(
    VpcIds=[
        'vpc-01d331832bab935c4',
    ],
)

print (response)

