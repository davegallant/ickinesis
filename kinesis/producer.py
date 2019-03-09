from uuid import uuid4
import boto3


class KinesisProducer:
    def __init__(self, stream_name, kinesis_client=None):
        self.kinesis_client = kinesis_client or boto3.Session().client("kinesis")
        self.stream_name = stream_name

    def put_record(self, message, partition_key=None):
        self.kinesis_client.put_record(
            StreamName=self.stream_name,
            Data=message,
            PartitionKey=partition_key or uuid4().hex,
        )

    def put_records(self, messages):
        self.kinesis_client.put_records(StreamName=self.stream_name, Records=messages)
