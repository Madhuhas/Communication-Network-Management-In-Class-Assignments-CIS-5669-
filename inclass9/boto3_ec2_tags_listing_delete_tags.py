# Kotini Sai Madhuhas
print ('Kotini Sai Madhuhas delete tags')

import boto3

resource = boto3.resource('ec2')

instance_id='i-06863aff46df316e8'
instance=resource.Instance(instance_id)
tagList=instance.tags

# create a tag
TAGS= [
    {
        'Key': 'cost center',
        'Value': '206987' 
    }
]

instance.delete_tags (Tags=TAGS)
print('completed...')