'''

This file will create a ec2 instance from an existing AMI  


-- wait until the instance is ready
return the public IP address of ec2 created



import boto3

client = boto3.resource('ec2')

instance = client.create_instances(
                ImageId='ami-0ff2cb586a7231532',
                InstanceType='t2.micro',
                MaxCount=1,
                MinCount=1,
                KeyName='ec2-jenkins'
                )
     

import boto3

ec2 = boto3.resource('ec2', region_name='us-east-1', aws_access_key_id='AKIA3MHTZCNPBJU2T5GE', aws_secret_access_key='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')

instance = ec2.create_instances(
    ImageId='ami-0b78ca23ea18811c5',
    InstanceType='t2.micro',
    KeyName='jenkins-ec2',
    MinCount=1,
    MaxCount=1
)
print(instance[0].id)
'''


import boto3 as bt
import time
import os

ec2 = bt.resource('ec2', region_name='us-east-1', aws_access_key_id='AKIA3XS5W62NHVG6YFPD', aws_secret_access_key='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')
def create():
    instances = ec2.create_instances(
        ImageId='ami-00e3b499a61c50fed',
        InstanceType='t2.micro',
        KeyName=' jenkins-gitlab',
        MinCount=1,
        MaxCount=1
        )
    print(instances)

client = bt.client('ec2', region_name='us-east-1', aws_access_key_id='AKIA3XS5W62NHVG6YFPD', aws_secret_access_key='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')
def getAll():
    instances = client.describe_instances()
    for inst in instances['Reservations']:
        if len(inst['Instances'][0]['NetworkInterfaces']) != 0:
            public_ip = inst['Instances'][0]['NetworkInterfaces'][0]['Association']['PublicIp']
            print(f"public_ip={public_ip}")
            

create()

time.sleep(120)
            
getAll()


