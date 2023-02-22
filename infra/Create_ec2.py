'''

This file will create a ec2 instance from an existing AMI  


-- wait until the instance is ready
return the public IP address of ec2 created
'''

import boto3 as bt
import time
import os
import sys

ec2 = bt.resource('ec2', region_name='us-east-1', aws_access_key_id=sys.argv[2], aws_secret_access_key=sys.argv[3])
def create():
    instances = ec2.create_instances(
        ImageId=sys.argv[1],
        InstanceType='t2.micro',
        KeyName='jenkins-gitlab',
        MinCount=1,
        MaxCount=1
        )
    print(instances)

client = bt.client('ec2',  region_name='us-east-1', aws_access_key_id=sys.argv[2], aws_secret_access_key=sys.argv[3])
def getAll():
    instances = client.describe_instances()
    for inst in instances['Reservations']:
        if len(inst['Instances'][0]['NetworkInterfaces']) != 0:
            public_ip = inst['Instances'][0]['NetworkInterfaces'][0]['Association']['PublicIp']
            print(f"public_ip={public_ip}")
            

create()

time.sleep(360)
            
getAll()


