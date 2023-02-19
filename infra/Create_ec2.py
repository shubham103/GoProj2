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
     
'''
import boto3

ec2 = boto3.resource('ec2', region_name='us-east-1', aws_access_key_id='AKIAQJO7ZSYXRPIMM2W4', aws_secret_access_key='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')

instance = ec2.create_instances(
    ImageId='ami-0ff2cb586a7231532',
    InstanceType='t2.micro',
    KeyName='ec2-jenkins',
    MinCount=1,
    MaxCount=1
)

print(instance[0].id)
