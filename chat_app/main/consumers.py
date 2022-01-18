from channels.consumer import SyncConsumer, AsyncConsumer
from channels.exceptions import StopConsumer 

class MysynConsumer(SyncConsumer):
	def websocket_connect(self, event):
		print("establisted connection",event)
		self.send({
			"type":"websocket.accept"
			})

	def websocket_receive(self, event):
		print("socket_recieved", event)
		print(event['text'])
		self.send({
			"type":"websocket.send",
			"text":"first websocket tested",
			})
	def websocket_disconnect(self, event):
		print("disconnect")
		raise StopConsumer()


class MyasynConsumer(AsyncConsumer):
	async def websocket_connect(self, event):
		print("establisted connection",event)
		await self.send({
			"type":"websocket.accept"
			})

	async def websocket_receive(self, event):
		print("socket_recieved", event)
		print(event['text'])
		await self.send({
			"type":"websocket.send",
			"text":"first websocket tested",
			})
	async def websocket_disconnect(self, event):
		print("disconnect")
		raise StopConsumer()

	