import os
from constructs import Construct
from aws_cdk import (
    aws_ssm as ssm,
    aws_ec2 as ec2,
    aws_s3 as s3,
    aws_iam as iam,
    aws_elasticloadbalancingv2  as elbv2,
    aws_autoscaling as autoscaling,
    Stack
)


class kolconstants(Stack):
  PROJECT="kol"
  CFN_PROJECT="kol"
  CFN_S3_STACK=PROJECT+"-s3-stack"
  CFN_IAM_STACK=PROJECT+"-iam-stack"
  CFN_ECR_STACK=PROJECT+"-ecr-stack"
  CFN_ECS_STACK=PROJECT+"-ecs-stack"
  CFN_KMS_STACK=PROJECT+"-kms-stack"
  CFN_SG_STACK=PROJECT+"-sg-stack"
  CFN_ELB_STACK=PROJECT+"-elb-stack"
  CFN_SSM_STACK=PROJECT+"-ssm-stack"
  CFN_DYNAMO_STACK=PROJECT+"-dynamo-failed-events-stack"
  CFN_SUMOSHIP_STACK=PROJECT+"-sumoship-stack"
  CFN_INFRA_STACK=PROJECT+"-infra-stack"

  def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
    super().__init__(scope, construct_id, **kwargs)
    env ="dev"
    environment ="dev"
    project ="kol"
