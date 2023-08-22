import asyncio
# 웹 소켓 모듈을 선언한다.
import websockets
import json
import datetime
import time
import asyncio


# 클라이언트 접속이 되면 호출된다.

async def connect():
  # 웹 소켓에 접속을 합니다.
  print("In")
  async with websockets.connect("ws://192.168.238.233:5000/gps") as websocket:
        # 클라이언트로부터 메시지를 대기한다.
        # text = input("Input: ")
        # 클라인언트로 echo를 붙여서 재 전송한다.
        print("Hello")
        while True:
            await websocket.send(json.dumps({"message":"hi","timeStamp":datetime.datetime.now().strftime("%H-%M-%S.%f")}))
            await asyncio.sleep(0)
            print(
                f'Sent message.{json.dumps({"message": "python", "timeStamp": datetime.datetime.now().strftime("%H-%M-%S.%f")})}')

            # await websocket.recv()
            time.sleep(0.1)

# 웹 소켓 서버 생성.호스트는 localhost에 port는 9998로 생성한다.
asyncio.get_event_loop().run_until_complete(connect());
