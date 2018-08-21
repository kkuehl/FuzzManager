# data exported from: https://ec2instances.info/ at 2018-08-16 17:54:16 UTC .. see disclaimers

import collections


InstanceType = collections.namedtuple("InstanceType", ("api_name", "vCPUs"))


INSTANCE_TYPES = (
    InstanceType("c1.medium", 2),
    InstanceType("c1.xlarge", 8),
    InstanceType("c3.2xlarge", 8),
    InstanceType("c3.4xlarge", 16),
    InstanceType("c3.8xlarge", 32),
    InstanceType("c3.large", 2),
    InstanceType("c3.xlarge", 4),
    InstanceType("c4.2xlarge", 8),
    InstanceType("c4.4xlarge", 16),
    InstanceType("c4.8xlarge", 36),
    InstanceType("c4.large", 2),
    InstanceType("c4.xlarge", 4),
    InstanceType("c5.18xlarge", 72),
    InstanceType("c5.2xlarge", 8),
    InstanceType("c5.4xlarge", 16),
    InstanceType("c5.9xlarge", 36),
    InstanceType("c5.large", 2),
    InstanceType("c5.xlarge", 4),
    InstanceType("c5d.18xlarge", 72),
    InstanceType("c5d.2xlarge", 8),
    InstanceType("c5d.4xlarge", 16),
    InstanceType("c5d.9xlarge", 36),
    InstanceType("c5d.large", 2),
    InstanceType("c5d.xlarge", 4),
    InstanceType("cc2.8xlarge", 32),
    InstanceType("cr1.8xlarge", 32),
    InstanceType("d2.2xlarge", 8),
    InstanceType("d2.4xlarge", 16),
    InstanceType("d2.8xlarge", 36),
    InstanceType("d2.xlarge", 4),
    InstanceType("f1.16xlarge", 64),
    InstanceType("f1.2xlarge", 8),
    InstanceType("g2.2xlarge", 8),
    InstanceType("g2.8xlarge", 32),
    InstanceType("g3.16xlarge", 64),
    InstanceType("g3.4xlarge", 16),
    InstanceType("g3.8xlarge", 32),
    InstanceType("h1.16xlarge", 64),
    InstanceType("h1.2xlarge", 8),
    InstanceType("h1.4xlarge", 16),
    InstanceType("h1.8xlarge", 32),
    InstanceType("hs1.8xlarge", 16),
    InstanceType("i2.2xlarge", 8),
    InstanceType("i2.4xlarge", 16),
    InstanceType("i2.8xlarge", 32),
    InstanceType("i2.xlarge", 4),
    InstanceType("i3.16xlarge", 64),
    InstanceType("i3.2xlarge", 8),
    InstanceType("i3.4xlarge", 16),
    InstanceType("i3.8xlarge", 32),
    InstanceType("i3.large", 2),
    InstanceType("i3.metal", 72),
    InstanceType("i3.xlarge", 4),
    InstanceType("m1.large", 2),
    InstanceType("m1.medium", 1),
    InstanceType("m1.small", 1),
    InstanceType("m1.xlarge", 4),
    InstanceType("m2.2xlarge", 4),
    InstanceType("m2.4xlarge", 8),
    InstanceType("m2.xlarge", 2),
    InstanceType("m3.2xlarge", 8),
    InstanceType("m3.large", 2),
    InstanceType("m3.medium", 1),
    InstanceType("m3.xlarge", 4),
    InstanceType("m4.10xlarge", 40),
    InstanceType("m4.16xlarge", 64),
    InstanceType("m4.2xlarge", 8),
    InstanceType("m4.4xlarge", 16),
    InstanceType("m4.large", 2),
    InstanceType("m4.xlarge", 4),
    InstanceType("m5.12xlarge", 48),
    InstanceType("m5.24xlarge", 96),
    InstanceType("m5.2xlarge", 8),
    InstanceType("m5.4xlarge", 16),
    InstanceType("m5.large", 2),
    InstanceType("m5.xlarge", 4),
    InstanceType("m5d.12xlarge", 48),
    InstanceType("m5d.24xlarge", 96),
    InstanceType("m5d.2xlarge", 8),
    InstanceType("m5d.4xlarge", 16),
    InstanceType("m5d.large", 2),
    InstanceType("m5d.xlarge", 4),
    InstanceType("p2.16xlarge", 64),
    InstanceType("p2.8xlarge", 32),
    InstanceType("p2.xlarge", 4),
    InstanceType("p3.16xlarge", 64),
    InstanceType("p3.2xlarge", 8),
    InstanceType("p3.8xlarge", 32),
    InstanceType("r3.2xlarge", 8),
    InstanceType("r3.4xlarge", 16),
    InstanceType("r3.8xlarge", 32),
    InstanceType("r3.large", 2),
    InstanceType("r3.xlarge", 4),
    InstanceType("r4.16xlarge", 64),
    InstanceType("r4.2xlarge", 8),
    InstanceType("r4.4xlarge", 16),
    InstanceType("r4.8xlarge", 32),
    InstanceType("r4.large", 2),
    InstanceType("r4.xlarge", 4),
    InstanceType("r5.12xlarge", 48),
    InstanceType("r5.24xlarge", 96),
    InstanceType("r5.2xlarge", 8),
    InstanceType("r5.4xlarge", 16),
    InstanceType("r5.large", 2),
    InstanceType("r5.xlarge", 4),
    InstanceType("r5d.12xlarge", 48),
    InstanceType("r5d.24xlarge", 96),
    InstanceType("r5d.2xlarge", 8),
    InstanceType("r5d.4xlarge", 16),
    InstanceType("r5d.large", 2),
    InstanceType("r5d.xlarge", 4),
    InstanceType("t1.micro", 1),
    InstanceType("t2.2xlarge", 8),
    InstanceType("t2.large", 2),
    InstanceType("t2.medium", 2),
    InstanceType("t2.micro", 1),
    InstanceType("t2.nano", 1),
    InstanceType("t2.small", 1),
    InstanceType("t2.xlarge", 4),
    InstanceType("x1.16xlarge", 64),
    InstanceType("x1.32xlarge", 128),
    InstanceType("x1e.16xlarge", 64),
    InstanceType("x1e.2xlarge", 8),
    InstanceType("x1e.32xlarge", 128),
    InstanceType("x1e.4xlarge", 16),
    InstanceType("x1e.8xlarge", 32),
    InstanceType("x1e.xlarge", 4),
    InstanceType("z1d.12xlarge", 48),
    InstanceType("z1d.2xlarge", 8),
    InstanceType("z1d.3xlarge", 12),
    InstanceType("z1d.6xlarge", 24),
    InstanceType("z1d.large", 2),
    InstanceType("z1d.xlarge", 4)
)


REGIONS = (
    "ap-northeast-1",
    "ap-northeast-2",
    "ap-south-1",
    "ap-southeast-1",
    "ap-southeast-2",
    "ca-central-1",
    "eu-central-1",
    "eu-west-1",
    "eu-west-2",
    "eu-west-3",
    "sa-east-1",
    "us-east-1",
    "us-east-2",
    "us-west-1",
    "us-west-2"
)


CORES_PER_INSTANCE = {instance.api_name: instance.vCPUs for instance in INSTANCE_TYPES}
