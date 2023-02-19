'''

This file will create a ec2 instance from an existing AMI  


-- wait until the instance is ready
return the public IP address of ec2 created

'''


import boto3

ec2 = boto3.resource('ec2')

instances = ec2.create_instances(
        ImageId="ami-0ff2cb586a7231532",
        MinCount=1,
        MaxCount=1,
        InstanceType="t2.micro",
        KeyName="ec2-jenkins"
    )
     
