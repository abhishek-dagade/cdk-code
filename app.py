#!/usr/bin/env python3
import os

import aws_cdk as cdk
from constants import kolconstants

from cdk_sandbox.cdk_sandbox_stack import kols3stack


app = cdk.App()
kols3stack(app, kolconstants.CFN_S3_STACK)

app.synth()
