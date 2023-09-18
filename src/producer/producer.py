import json
import os
from aiokafka import AIOKafkaProducer


async def send_message(script_name, parameters, collection):
    bootstrap_servers = os.getenv('KAFKA_BOOTSTRAP_SERVER')
    topic = 'parsers_topic'
    producer = AIOKafkaProducer(bootstrap_servers=bootstrap_servers)
    await producer.start()

    message = {
        'script_name': script_name,
        'parameters': parameters,
        'collection': collection,
    }

    try:
        message_str = json.dumps(message)
        await producer.send_and_wait(topic, value=message_str.encode('utf-8'))
    finally:
        await producer.stop()
