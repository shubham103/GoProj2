'''

This file will create a ec2 instance from an existing AMI  


-- wait until the instance is ready
return the public IP address of ec2 created
'''
import boto3 as bt
import time
import os
import sys
import requests
import base64



ec2 = bt.resource('ec2', region_name='us-east-1', aws_access_key_id='AKIA3TRJZGPS266EZ7US', aws_secret_access_key='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')

client = bt.client('ec2', region_name='us-east-1', aws_access_key_id='AKIA3TRJZGPS266EZ7US', aws_secret_access_key='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')


#ec2 = bt.resource('ec2', region_name='us-east-1', aws_access_key_id=sys.argv[2], aws_secret_access_key=sys.argv[3])
#client = bt.client('ec2',  region_name='us-east-1', aws_access_key_id=sys.argv[2], aws_secret_access_key=sys.argv[3])



def create():

    instances = ec2.create_instances(ImageId='ami-01fa04d1f425b3c15',InstanceType='t2.micro',KeyName='jenkins-gitlab',MinCount=1,MaxCount=1, SecurityGroupIds=['sg-020cd77a656cf2625',])
    '''instances = ec2.create_instances(
        ImageId=sys.argv[1],
        InstanceType='t2.micro',
        KeyName='jenkins-gitlab',
        MinCount=1,
        MaxCount=1,
        SecurityGroupIds=[sys.argv[4],],
        )
    '''
    print(instances)

def find_ip():

    instances = client.describe_instances()
    for inst in instances['Reservations']:
        if len(inst['Instances'][0]['NetworkInterfaces']) != 0:
            #print(inst['Instances'][0]['NetworkInterfaces'][0].keys())
            while True:
                print("checking association")
                time.sleep(3)
                if 'Association' in inst['Instances'][0]['NetworkInterfaces'][0].keys():
                    print("association found")
                    break
        
            public_ip = inst['Instances'][0]['NetworkInterfaces'][0]['Association']['PublicIp']
            return public_ip

create()
time.sleep(6)
public_ip = find_ip()
jenkins_url = f"http://{public_ip}:8080"
username = "shubham"
api_token = "11d4713c7830dcab9c483c7be03eab78b0"

auth_string = base64.b64encode(f"{username}:{api_token}".encode()).decode()

headers = {
    "Authorization": f"Basic {auth_string}"
}

while True:
    print("connecting url")
    response = requests.get(jenkins_url, headers=headers)
    print("fetching response url", response.status_code)
    if response.status_code == 200:
        print("Jenkins server is available!")
        break
