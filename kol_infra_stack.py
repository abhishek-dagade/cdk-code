from constants import kolconstants
from aws_cdk import (
    Duration,
    Stack,
    aws_s3 as s3
)
#import aws_cdk as core

class KolInfraStack(Stack):

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

        #raw_image_bucket_name = "-".join("a",[project.lower(),environment.lower(),"raw","images"])

        s3_bucket = s3.CfnBucket(
            self, "kol-raw-images",
            #bucket_name=raw_image_bucket_name,
            bucket_name="test-090901",
            public_access_block_configuration=public_access_block_configuration_property,
            bucket_encryption=bucket_encryption_property
        )

        s3_bucket = s3.Bucket(
            self, "kol-raw-image-mapping",
            #bucket_name="kol-dev-product-image-mapping"
            bucket_name="test-889977"
        )
