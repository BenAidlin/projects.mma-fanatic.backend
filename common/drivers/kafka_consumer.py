from common.adapters.kafka_client import KafkaClient

if __name__ == "__main__":
    consumer = KafkaClient('localhost:9092', 'test-topic')
    consumer.consume_messages(callback=lambda message: print(f"Received message: {message}"))