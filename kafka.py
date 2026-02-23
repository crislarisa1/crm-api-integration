from kafka import KafkaProducer
import json

producer = KafkaProducer(
    bootstrap_servers=['kafka-broker1:9092', 'kafka-broker2:9092'],
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

producer.send(
    'checkout-events',
    evento_padronizado
)

producer.flush()
