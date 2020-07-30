import json
import os

import boto3

os.environ["AWS_PROFILE"] = "prof1"
s3 = boto3.client("s3")


def aws_sample():
    RESPONSE = s3.list_buckets()

    for bucket in RESPONSE["Buckets"]:
        print(f'{bucket["Name"]}')

    # bucket = s3.bucket("iwato-sample")
    # file_path = "sample/sample.json"
    #
    # json_object = {"sample": "sample1", "number": 987654321}
    # json_str = json.dumps(json_object)
    # bucket.upload_file("""  aaaa """, file_path)


if __name__ == "__main__":
    aws_sample()
