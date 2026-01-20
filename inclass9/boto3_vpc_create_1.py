# Kotini Sai Madhuhas
print ('Kotini Sai Madhuhas boto3 vpc')

import boto3

resource = boto3.resource('ec2')

#create VPC
vpc = resource.create_vpc (CidrBlock='172.16.0.0/16')

# assign a name tag
vpc.create_tags (
    Tags=[
        {"Key":"Name","Value": "kotini VPC Pythhon Boto3"}
    ]
)

# wait until vpc is available
vpc.wait_until_available();

# update dns host name
client = boto3.client('ec2')
client.modify_vpc_attribute(VpcID = vpc.id, EnableDnsSupport={ 'Value':True})
client.modify_vpc_attribute(VpcID = vpc.id, EnableDnsHostnames={ 'Value':True})