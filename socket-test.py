import socket
from datetime import datetime
import json
import time


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.connect(('192.168.238.233', 5001))     # 접속할 서버의 ip주소와 포트번호를 입력.

while True :
    sock.send(json.dumps({"message":"python","timeStamp":datetime.now().strftime("%H-%M-%S.%f")}).encode())
    print("Send!")
    time.sleep(0.1)