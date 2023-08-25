import socket
from datetime import datetime
import json
import time
import base64
import os

#6ms ~ 10ms

if not os.name.startswith("nt"):
    HOST_NAME = "192.168.238.233"
else :

    print("You're in Window!")
    HOST_NAME = "localhost"

CHUNK_SIZE = 1024*1024*10

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.connect((HOST_NAME, 5001))     # 접속할 서버의 ip주소와 포트번호를 입력.

with open("test.png", "rb") as image_file:
    image_binary = image_file.read()
    encoded_img = base64.b64encode(image_binary).decode("utf-8")


while True :

    raw_byte_data = json.dumps({"message":encoded_img,"timeStamp":datetime.now().strftime("%H-%M-%S.%f")}).encode()
    chunk_list = []

    for idx in range(0,len(raw_byte_data),CHUNK_SIZE):
        sock.sendall(raw_byte_data[idx:idx+CHUNK_SIZE])
    # print("Send Blank!")
    time.sleep(0.1)

    print("Send!")
