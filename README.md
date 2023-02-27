## Prerequisite:
- Jenkins AMI should exist in aws with jenkins installed, s3 plugin configured and golang installed.



## Workflow
![Blank diagram (2)](https://user-images.githubusercontent.com/26185774/218420134-4b7811c4-25d7-44e1-b49f-39a27d408be9.png)


## Things need to study 
- How to make github actions wait for jenkins to finish its job
- How to use aws Simple Email Service to send mails from jenkins.
- How to pass the information of ec2 instance created in first step of github action to the last step of github action to terminate the ec2.
    - created single python script for creating ec2 instance, triggering pipeline , waiting for pipline and then terminating the ec2.
