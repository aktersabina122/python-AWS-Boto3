
# Create EC2 instance

import boto3

ec2 = boto3.resource("ec2")
"""instances = ec2.create_instances(
    ImageId = "ami-0b0dcb5067f052a63",
    InstanceType = "t2.micro",
    MinCount = 3,
    MaxCount = 3,
    KeyName = "KeyPair1",
    TagSpecifications = [
        {
            'ResourceType': 'instance',
            'Tags' : [{"Key": "Environment", "Value": "Prod"}]
      
        },
    ],
   
    )


print ("EC2 instances have been created Successsfully in AWS")
"""

# Terminate EC2 instances
ec2.instances.filter(InstanceIds=["i-0b10a6d1fd76e3d2c", "i-0df5b736a602f3298"]).terminate()
print("Instances terminate successfully")

# Stop EC2 instacnes
ec2.instances.filter(InstanceIds=["i-01a7d9857d956f926"]).stop()
#print("Instances stopped successfully")

# Start EC2 instacnes
ec2.instances.filter(InstanceIds=["i-01a7d9857d956f926"]).start()
print("Instances started successfully")


