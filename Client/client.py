import threading
import socket

class ThreadedTcpSocketClient(threading.Thread):
	def __init__(self, ip, port, socket):
		threading.Thread.__init__(self)
		self.ip = ip
		self.port = port
		self.socket = socket
	def run(self):
		self.socket.connect((self.ip, self.port))
		data = self.socket.recv(32).decode("utf-8")
		if data == "01":
			print("Success")
		elif data == "02":
			print("Invalid login")
		elif data == "03":
			print("User has been taked")
	def send(self, content):
		self.socket.send(content)
