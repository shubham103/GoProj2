import boto3 as bt
import time
import os
import sys
import requests
import base64
import json


aws_key = sys.argv[1] #'AKIAWAJCMNOWMM35I6QA'
aws_secret = sys.argv[2] #'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'
img_id = sys.argv[3] #'ami-0fa014fa43e187615'
security_grp = sys.argv[4] #'sg-08d8e924cafcb70d5'
api_token = sys.argv[5] #"1112e0bacf1607032ff5d648dae12d05e7"

# create clients

ec2 = bt.resource('ec2', region_name='us-east-1', aws_access_key_id=aws_key, aws_secret_access_key=aws_secret)

client = bt.client('ec2', region_name='us-east-1', aws_access_key_id=aws_key, aws_secret_access_key=aws_secret)

#  create jenkins-ec2-instance
def create():
    instances = ec2.create_instances(ImageId=img_id,InstanceType='t2.micro',KeyName='jenkins-gitlab',MinCount=1,MaxCount=1, SecurityGroupIds=[security_grp,])
    
    print("Instance ID :",instances[0].id)
    return instances[0].id
    
instance_id=create()
time.sleep(5)

#  fetch the ip address of the new instance

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
            
public_ip = find_ip()

#  wait for the server to come up
jenkins_url = f"http://{public_ip}:8080"
username = "shubham"
auth_string = base64.b64encode(f"{username}:{api_token}".encode()).decode()
headers = { "Authorization": f"Basic {auth_string}"}
while True:
    print(f"connecting url {jenkins_url}")
    time.sleep(3)
    try:
        response = requests.get(jenkins_url, headers=headers, timeout=5)
        print("fetching response url", response.status_code)
        if response.status_code == 200:
            print("Jenkins server is available!")
            break
    except:
        print("Time out :: connecting again")
    
    

#  get the last build of jenkins

jenkins_lastbuild_url = f"http://{public_ip}:8080/job/build/lastBuild/buildNumber"
response = requests.get(jenkins_lastbuild_url, headers=headers)
try:
    if not '404' in response.text:
        print("last_build=",response.text)
    next_build = int(response.text.strip())+1
    print(f"next_build={next_build}")
except:
    print("No build exists")
    next_build = 1
    print(f"next_build={next_build}")

#  trigger the new build

jenkins_trigger_url = f"http://{public_ip}:8080/job/build/build?token=test1234"
jenkins_build_status_url = f"http://{public_ip}:8080/job/build/{next_build}/api/json"
requests.get(jenkins_trigger_url, headers=headers)
    
#  wait untill the new build finishes

while True:
    
    response = requests.get(jenkins_build_status_url, headers=headers)
    if response.status_code == 200:
        data = json.loads(response.text.strip())
        if data['result'] != None:
            print(f"Pipeline finished with status code: {data['result']}")
            break
        else:
            print("waiting for pipeline to finish")
    else:
    	print("waiting for pipeline to start")
    time.sleep(1)

#  terminate the jenkins-ec2-instance


print("Terminating the instance")
response = client.terminate_instances(InstanceIds=[instance_id])
