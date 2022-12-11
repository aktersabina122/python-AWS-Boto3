
# Create script to terminate the EC2 instance
"""import boto3
 
ec2 = boto3.client('ec2')

response = ec2.terminate_instances(
	    InstanceIds=[
        'i-0961ba79d89c5c4fd','i-0fd748fad07ab0fdf','i-07d08e9ebcae2a3c1',
    ],
)

"""



import boto3
import Constant

ec2 = boto3.client('ec2',
                    'us-east-1',
                    aws_access_key_id=constant.aws_access_key_id,
                    aws_secret_access_key=constant.aws_secret_access_key)

"""""
ids = ['i-0b10a6d1fd76e3d2c','i-0df5b736a602f3298','i-01a7d9857d956f926']
ec2 = boto3.resource('ec2')

ec2.instances.filter(InstanceIds = ids).stop()

print ("Your instances have been successfully terminated")
"""

instances=["i-0b10a6d1fd76e3d2c","i-01a7d9857d956f926","i-0df5b736a602f3298"]
# Stop EC2 instacnes
ec2.stop_instances(instanceIds=instances)
print("Instances stop successfully")

# Start EC2 instacnes
#instances = ec2.start_instances(instanceIds=instances)
#print("Instances start successfully")

# Terminate EC2 instances
#instances = ec2.terminate_instances(instanceIds=instances)
#print("Instances terminate successfully")
