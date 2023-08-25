import asyncio
# 웹 소켓 모듈을 선언한다.
import websockets
import json
import datetime
import time
import asyncio
import os
import base64
print(os.name)

#10ms ~ 15ms

if not os.name.startswith("nt"):
    HOST_NAME = "192.168.238.233:5000"

else :

    print("You're in Window!")
    HOST_NAME = "localhost:5000"


# 클라이언트 접속이 되면 호출된다.

async def connect():
  # 웹 소켓에 접속을 합니다.
  async with websockets.connect(f"ws://{HOST_NAME}/gps",write_limit=1024*1024*10) as websocket:
        # 클라이언트로부터 메시지를 대기한다.
        # text = input("Input: ")
        # 클라인언트로 echo를 붙여서 재 전송한다.
        print("Hello")

        with open("test.png", "rb") as image_file:
            image_binary = image_file.read()
            encoded_img = base64.b64encode(image_binary).decode()


        while True:
            await websocket.send(json.dumps({"message":encoded_img,"timeStamp":datetime.datetime.now().strftime("%H-%M-%S.%f")}),)
            await asyncio.sleep(0)
            print(
                f'Sent message.{json.dumps({"timeStamp": datetime.datetime.now().strftime("%H-%M-%S.%f")})}')

            # await websocket.recv()
            time.sleep(0.1)

# 웹 소켓 서버 생성.호스트는 localhost에 port는 9998로 생성한다.
asyncio.get_event_loop().run_until_complete(connect());
