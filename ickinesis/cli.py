"""Improved Color Kinesis"""

import atexit
import json
import os
import sys
from datetime import datetime
from kafka import KafkaConsumer
from pygments import highlight
from pygments.formatters import TerminalFormatter  # pylint: disable-msg=E0611
from pygments.lexers import JsonLexer  # pylint: disable-msg=E0611
from ickinesis.config import create_config_dir, CAPTURES_FOLDER
from ickinesis.input import get_args

ARGUMENTS = get_args()
MESSAGES_CAPTURED = []


def start_consumer(arguments):

    # start consuming them bytes
    consumer = KafkaConsumer(
        arguments.topic,
        auto_offset_reset=arguments.offset,
        bootstrap_servers=[arguments.server],
        enable_auto_commit=True,
        group_id=arguments.group,
    )

    # print each message that is consumed
    for count, message in enumerate(consumer, 1):
        message = message.value.decode("utf-8")
        try:
            message = json.loads(message)
            message = json.dumps(message, indent=4, sort_keys=True)
            if arguments.no_color:
                print(message)
            else:
                print(highlight(message, JsonLexer(), TerminalFormatter()))
            MESSAGES_CAPTURED.append(json.loads(message))
        except Exception:  # pylint: disable=broad-except
            print(message)
            MESSAGES_CAPTURED.append(message)
        print("messages consumed: {}".format(count))
        print("")


def exit_handler():
    if not ARGUMENTS.version:
        print("")
        print("Shutting down consumer...")
    # If there are captured messages and the capture flag is set to true,
    # dump messages as a json array
    if MESSAGES_CAPTURED and ARGUMENTS.capture:
        json_dumped_file = "{}/{}_{}.json".format(
            CAPTURES_FOLDER, ARGUMENTS.topic, datetime.utcnow().isoformat()
        )
        print("")
        print("Dumping consumed messages into: %s" % json_dumped_file)
        print("")
        with open(json_dumped_file, "w") as outfile:
            json.dump(MESSAGES_CAPTURED, outfile, sort_keys=True, indent=4)
    try:
        sys.exit(os.EX_OK)
    except SystemExit:
        os._exit(os.EX_OK)


atexit.register(exit_handler)

try:
    create_config_dir()
    start_consumer(arguments=ARGUMENTS)

except KeyboardInterrupt:
    exit_handler()
