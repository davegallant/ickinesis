from collections import deque
from random import randint
import boto3


class KinesisProducer:
    def __init__(
        self, stream_name: str, max_queue: int = 500, client: str = None
    ) -> None:
        self._client = client or boto3.client("kinesis")
        self._stream_name = stream_name
        self.queue = deque()
        self._max_queue = max_queue

    @staticmethod
    def random_partition() -> str:
        return randint(0, 10 ** 12).__str__()

    def put_record(self, message: str) -> None:
        self._client.put_record(
            StreamName=self._stream_name,
            Data=message,
            PartitionKey=self.random_partition(),
        )

    def queue_message(self, message: str) -> None:
        self.queue.append({"Data": message, "PartitionKey": self.random_partition()})
        if len(self.queue) >= self._max_queue:
            self.flush()

    def flush(self) -> None:
        if self.queue:
            self._client.put_records(
                Records=list(self.queue), StreamName=self._stream_name
            )
            self.queue.clear()
