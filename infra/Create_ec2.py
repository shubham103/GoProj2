'''

This file will create a ec2 instance from an existing AMI  


-- wait until the instance is ready
return the public IP address of ec2 created

'''


import boto3

client = boto3.resource('ec2')

instance = client.create_instances(
                ImageId='ami-0ff2cb586a7231532',
                InstanceType='t2.micro',
                MaxCount=1,
                MinCount=1,
                KeyName='ec2-jenkins'
                )
     
