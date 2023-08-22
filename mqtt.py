import json
from datetime import datetime
import pika
import time


HOST_NAME = "localhost"
QUEUE_NAME = "hello.queue"


def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters(host=HOST_NAME))
    channel = connection.channel()

    channel.queue_declare(queue=QUEUE_NAME)

    while True:

        channel.basic_publish(exchange='hello.exchange', routing_key="hello.key", body=json.dumps({"message":"python","timeStamp":datetime.now().strftime("%H-%M-%S.%f")}))
        print(f'Sent message.{json.dumps({"message":"python","timeStamp":datetime.now().strftime("%H-%M-%S.%f")})}')
        time.sleep(0.1)
    connection.close()

if __name__ == '__main__':
    main()