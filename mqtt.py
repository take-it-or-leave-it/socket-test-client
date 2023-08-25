import json
from datetime import datetime
import pika
import time
import os
import base64


#3ms ~ 5ms


print(os.name)

if not os.name.startswith("nt"):
    HOST_NAME = "192.168.238.233"
    user_credentials = pika.PlainCredentials('rasp', '1234')
else :

    print("You're in Window!")
    HOST_NAME = "localhost"
    user_credentials = pika.PlainCredentials('guest', 'guest')


QUEUE_NAME = "hello.queue"

def main():
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(
            host=HOST_NAME,
            credentials=user_credentials
            )

        )
    channel = connection.channel()

    channel.queue_declare(queue=QUEUE_NAME)

    with open("test.png", "rb") as image_file:
        image_binary = image_file.read()
        encoded_img = base64.b64encode(image_binary).decode()


    while True:

        channel.basic_publish(exchange='hello.exchange', routing_key="hello.key", body=json.dumps({"message":encoded_img,"timeStamp":datetime.now().strftime("%H-%M-%S.%f")}))
        print(f'Sent message.{json.dumps({"timeStamp":datetime.now().strftime("%H-%M-%S.%f")})}')
        time.sleep(0.1)
    connection.close()

if __name__ == '__main__':
    main()