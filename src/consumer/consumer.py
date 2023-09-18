import os
import asyncio
import json
from aiokafka import AIOKafkaConsumer

from src.parsers.lamoda_parsers import parse_lamoda_items
from src.exceptions.custom_exception import CustomExceptionHandler
from src.parsers.twitch_parsers import parse_twitch_games, parse_twitch_streams
from src.config.dependencies import get_database


async def process_message(message: str):
    message = json.loads(message)

    script_name = message['script_name']
    params = message['parameters']
    collection = message['collection']

    database = get_database()
    if script_name == "lamoda_parser":
        try:
            for page in range(1, params['pages'] + 1):
                await parse_lamoda_items(database, params['url'], page)
        except Exception as e:
            raise CustomExceptionHandler(detail='Lamoda url is incorrect', status_code=400)

    elif script_name == "twitch_parser":
        if collection == "games":
            try:
                await parse_twitch_games(database)
            except Exception as e:
                raise CustomExceptionHandler(detail="Game Parsing Error", status_code=500)
        elif collection == "streams":
            try:
                await parse_twitch_streams(database)
            except Exception as e:
                raise CustomExceptionHandler(detail="Stream Parsing Error", status_code=500)
        else:
            print("Unknown collection name:", collection)
    else:
        print("Unknown script name:", script_name)


async def read_messages():
    bootstrap_servers = os.getenv('KAFKA_BOOTSTRAP_SERVER')
    topic = 'parsers_topic'
    loop = asyncio.get_event_loop()
    consumer = AIOKafkaConsumer(topic, bootstrap_servers=bootstrap_servers, loop=loop)
    await consumer.start()
    try:
        async for message in consumer:
            await process_message(message.value.decode('utf-8'))
    finally:
        await consumer.stop()
