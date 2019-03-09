import boto3
import pytest
from moto import mock_kinesis


@pytest.fixture(scope="module")
def kinesis():
    mock = mock_kinesis()
    mock.start()
    client = boto3.client("kinesis", region_name="ca-central-1")
    client.create_stream(StreamName="test-stream", ShardCount=2)
    yield client
    mock.stop()
