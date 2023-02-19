'''

This file will create a ec2 instance from an existing AMI  


-- wait until the instance is ready
return the public IP address of ec2 created

'''


import boto3

ec2 = boto3.client('ec2')

print(ec2)
