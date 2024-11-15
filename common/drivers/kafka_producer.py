from common.adapters.kafka_client import KafkaClient

if __name__ == "__main__":
    producer = KafkaClient('localhost:9092', 'test-topic')
    for i in range(1000):
        producer.produce_message(str(i))