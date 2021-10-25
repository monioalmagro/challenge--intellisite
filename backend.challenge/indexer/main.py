import os
import json
from kafka import KafkaConsumer, KafkaProducer

from mongo import index_to_database


KAFKA_BROKER_URL = os.environ.get("KAFKA_BROKER_URL")
DETECTIONS_TOPIC = os.environ.get("DETECTIONS_TOPIC")
DETECTIONS_TOPIC_2 = 'intellisite.alerts'


producer = KafkaProducer(
    bootstrap_servers=KAFKA_BROKER_URL,
    # Encode all values as JSON
    api_version=(0, 11, 5),
    value_serializer=lambda value: json.dumps(value).encode(),
)

consumer = KafkaConsumer(DETECTIONS_TOPIC, api_version=(0, 11, 5), bootstrap_servers=KAFKA_BROKER_URL)
for message in consumer:
    mess = json.loads(message.value.decode('utf-8'))
    if mess.get('Category') == 'SUV':
        producer.send(DETECTIONS_TOPIC_2, value=mess)
        producer.flush()
    index_to_database(mess)

