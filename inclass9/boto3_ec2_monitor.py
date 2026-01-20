# Kotini Sai Madhuhas
print ('Kotini Sai Madhuhas boto3 monitor')

import boto3

resource = boto3.resource('ec2')

instance_id='i-06863aff46df316e8'
#instance=resource.Instance(instance_id)

instances=resource.instances.filter(
    InstanceIds=[
        instance_id,
    ]
)

for instance in instances:
    monitor_status=instance.monitoring['State']
    print('Monitor status ' + monitor_status)
    if  monitor_status == "enabled":
        print('Monitor Enabled...')
        instance.unmonitor()
    else:
        print('Monitor disabled...')
        instance.monitor()


print('completed...')