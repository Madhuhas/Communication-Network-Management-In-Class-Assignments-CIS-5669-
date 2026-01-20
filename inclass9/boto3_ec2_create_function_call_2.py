# Kotini Sai Madhuhas
print ('Kotini Sai Madhuhas EC2 using a function call')

import boto3

ec2 = boto3.resource('ec2')

def createEC2(ami, key_name, instance_type, max_count, min_count, tags_list, subnet_id):
    myInstance=''

    response=ec2.create_instances(
        ImageId=ami,
        KeyName=key_name,
        InstanceType=instance_type,
        MaxCount=max_count,
        MinCount=min_count,
        TagSpecifications=tags_list,
        SubnetId=subnet_id
    )
    
    for instance in response:
        myInstance=instance
        print('Launching instance, please wait...')
        myInstance.wait_until_running()
        print('Launching launched with ID: ' + myInstance.id)

    return myInstance

ami='ami-000c0df09737657b6'
key_name='KotiniUCM24'
instance_type='t2.micro'
max_count=1
min_count=1
tags_list=[
    {
        'ResourceType' : 'instance',
        'Tags' : [
           { 'Key' : 'Name',
            'Value' : 'Kotini EC2 Boto3 custom VPC'
            },
        ]
    },
]
subnet_id='subnet-00a652269720c58ce'
vpc_id='vpc-063b8b7035a676e55'

myInstance = createEC2(ami, key_name, instance_type, max_count, min_count, tags_list, subnet_id)
print("Call to create EC2 returned", myInstance.id)
