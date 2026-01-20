# Kotini Sai Madhuhas
print ('Kotini Sai Madhuhas boto3 modify instance')

import boto3

resource = boto3.resource('ec2')

instance_id='i-06863aff46df316e8'

keyname='KotiniKeyBoto3'
myTag=[
    {
        'ResourceType': 'key-pair',
        'Tags': [
            {'Key':'Name',
             'Value':'my-ssh-boto3-key-pair',
            },
        ]    
    },
]

key_pair=resource.create_key_pair(
    KeyName=keyname,
    TagSpecifications=myTag
)

print(f'fingerprint: {key_pair.key_fingerprint}')
print(f'private SSH key: {key_pair.key_material}')

key_pairs=resource.key_pairs.all()
for key in key_pairs:
    print(f'SSH key: {key.key_name}')

print('completed...')