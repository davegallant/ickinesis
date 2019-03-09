from kinesis.consumer import KinesisConsumer


def test_consume(kinesis):
    consumer = KinesisConsumer(kinesis_client=kinesis)
    consumer.consume("test-stream")
