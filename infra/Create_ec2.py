'''

This file will create a ec2 instance from an existing AMI  


-- wait until the instance is ready
return the public IP address of ec2 created
'''

import boto3 as bt
import time
import os

ec2 = bt.resource('ec2')
def create():
    instances = ec2.create_instances(
        ImageId='ami-06f8a75bec86e113b',
        InstanceType='t2.micro',
        KeyName='jenkins-gitlab',
        MinCount=1,
        MaxCount=1
        )
    print(instances)

client = bt.client('ec2')
def getAll():
    instances = client.describe_instances()
    for inst in instances['Reservations']:
        if len(inst['Instances'][0]['NetworkInterfaces']) != 0:
            public_ip = inst['Instances'][0]['NetworkInterfaces'][0]['Association']['PublicIp']
            print(f"public_ip={public_ip}")
            

create()

time.sleep(120)
            
getAll()


