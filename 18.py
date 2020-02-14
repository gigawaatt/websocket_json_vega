import websockets
import asyncio
import json


async def hello():
	uri = "ws://10.12.0.90:8002"
	async with websockets.connect(uri) as websocket:
		cmd1 = '{"cmd": "auth_req" , "login": "root" , "password": "123"}'
		cmd2 = '{"cmd": "get_data_req" , "devEui": "3137353264386C0A" , "select": "null"}'
		await websocket.send(cmd1)
		print(f"> {cmd1}")

		greeting = await websocket.recv()
		print(f"< {greeting}")

		await websocket.send(cmd2)
		print(f"> {cmd2}")

		greeting = await websocket.recv()
		greeting = await websocket.recv()
		

		data = json.loads(greeting)

		with open('response.json', 'w', encoding='utf-8') as file:
			json.dump(data, file, indent=2, ensure_ascii=False)



asyncio.get_event_loop().run_until_complete(hello())


