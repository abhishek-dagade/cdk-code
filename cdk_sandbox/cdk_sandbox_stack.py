from constants import kolconstants
from constructs import Construct
from aws_cdk import (
    Duration,
    Stack,
    aws_s3 as s3,
    aws_iam as iam
)

class kols3stack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        env ="dev"
        environment ="dev"
        project ="kol"


        public_access_block_configuration_property = s3.CfnBucket.PublicAccessBlockConfigurationProperty(
              block_public_acls=True,
              block_public_policy=True,
              ignore_public_acls=True,
              restrict_public_buckets=True
        )
        bucket_encryption_property = s3.CfnBucket.BucketEncryptionProperty(
            server_side_encryption_configuration=[s3.CfnBucket.ServerSideEncryptionRuleProperty(
                bucket_key_enabled=True,
                server_side_encryption_by_default=s3.CfnBucket.ServerSideEncryptionByDefaultProperty(
                    sse_algorithm="AES256",
                )
            )]
        )

        raw_image_bucket_name = "-".join([project.lower(),environment.lower(),"raw","images"])

        s3_bucket = s3.CfnBucket(
            self, "kol-raw-images",
            bucket_name=raw_image_bucket_name,
            #bucket_name="test-090901",
            public_access_block_configuration=public_access_block_configuration_property,
            bucket_encryption=bucket_encryption_property
        )

        image_mapping_bucket_name = "-".join([project.lower(),environment.lower(),"product","image","mapping"])

        s3_bucket = s3.CfnBucket(
            self, "kol-raw-image-mapping",
            bucket_name=image_mapping_bucket_name,
            #bucket_name="test-889977",
            #public_access_block_configuration=public_access_block_configuration_property,
            #bucket_encryption=bucket_encryption_property
        )

        s3_cross_account_access = iam.PolicyDocument(
            statements=[iam.PolicyStatement(
                    effect=iam.Effect.ALLOW,
                    sid="S3list",
                    actions=["s3:GetBucketLocation","s3:ListBucket"
                    ],               
                    resources=["*"]
                ),
                iam.PolicyStatement(
                    effect=iam.Effect.ALLOW,
                    sid="s3objectget",
                    actions=[
                    "s3:GetObject"
                    ],               
                    resources=["*"]
                )]
        )

        s3_cross_accont_trust_relationship = iam.PolicyDocument(
            statements=[
              iam.PolicyStatement(
                effect=iam.Effect.ALLOW,               
                actions=[
                  "sts:AssumeRole"
                ],                
                principals=[iam.ServicePrincipal("lambda.amazonaws.com")],
              ),
              iam.PolicyStatement(
                effect=iam.Effect.ALLOW,               
                actions=[
                  "sts:AssumeRole",            
                  "sts:TagSession"
                ],
                principals=[iam.ServicePrincipal("lambda.amazonaws.com")]
              )
            ]
        )

        s3_cross_account_access = iam.CfnRole(self, "PlmInfraRole",
            assume_role_policy_document=cfn_infra_role_trust_policy_document,
            role_name="s3_cross_account_access",
            description="role infra user",
            permissions_boundary="arn:aws:iam::494964762729:policy/AWSManagedServicesDevelopmentRolePermissionsBoundary",
            policies=[
                iam.CfnRole.PolicyProperty(policy_document=s3_cross_account_access,policy_name="s3_cross_account_access")
            ]
        )
