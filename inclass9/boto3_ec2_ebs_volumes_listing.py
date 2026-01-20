# Kotini Sai Madhuhas
print ('Kotini Sai Madhuhas ebs volume')

import boto3

resource = boto3.resource('ec2')

instance_id='i-06863aff46df316e8'
instance=resource.Instance(instance_id)
ebsList=instance.block_device_mappings

for ebs in ebsList:
    volume_id=ebs['Ebs']['VolumeId']
    volume_name=ebs['DeviceName']
    print("volume ID: "+volume_id+", name: "+volume_name)

print('completed...')
