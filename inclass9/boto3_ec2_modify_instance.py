# Kotini Sai Madhuhas
print ('Kotini Sai Madhuhas boto3 modify instance')

import boto3

resource = boto3.resource('ec2')

instance_id='i-06863aff46df316e8'

instances=resource.instances.filter(
    InstanceIds=[
        instance_id,
    ]
)

for instance in instances:
    instance.stop()
    instance.wait_until_stopped()

    instance.modify_attribute(
        InstanceType={
            'Value': 't2.micro',
        }
    )

    instance.start()
    instance.wait_until_stopped()
    #reboot
    instance.reboot()

print('completed...')