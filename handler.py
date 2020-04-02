import json
import boto3

asg = boto3.client('autoscaling')
ec2 = boto3.client('ec2')

def tag_asg_instances(event, context):
    print(event)

    asg_name = event["detail"]["AutoScalingGroupName"]
    instance_id = event["detail"]["EC2InstanceId"]

    r = asg.describe_auto_scaling_groups(AutoScalingGroupNames=[asg_name])
    tags = r['AutoScalingGroups'][0]['Tags']

    if not any(t['Key'] ==  'eks:nodegroup-name' for t in tags):
        print('not node group')
    else:
        v = [t['Value'] for t in tags if t['Key'] == 'eks:nodegroup-name'][0]
        r = ec2.create_tags(Resources=[instance_id], Tags=[{'Key':'Name', 'Value':v}])
        print(r)
    return
