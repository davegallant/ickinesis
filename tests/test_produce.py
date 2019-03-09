from kinesis.producer import KinesisProducer


def test_put_record(kinesis):
    kinesis_producer = KinesisProducer(
        stream_name="test-stream", kinesis_client=kinesis
    )
    kinesis_producer.put_record(message="fake message")
