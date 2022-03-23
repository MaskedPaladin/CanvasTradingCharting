import threading
import socket
import server_data_api as sda

class ThreadedTcpSocketServer(threading.Thread):
	def __init__(self, ip, port, socket):
		threading.Thread.__init__(self)
		self.ip = ip
		self.port = port
		self.socket = socket
	def run(self):
		self.socket.bind((self.ip, self.port))
		self.socket.listen()
		while True:
			connection, ip = self.socket.accept()
			data = connection.recv(32).decode("utf-8")
			print(data)
			command = data.split(",")
			if command[0] == "05":
				connection.send(sda.loadUser(command[1], command[2]).encode("utf-8"))
			elif command[0] == "06":
				connection.send(sda.insertUser(command[1], command[2], command[3]).encode("utf-8"))
		
server = ThreadedTcpSocketServer('localhost', 25565, socket.socket(socket.AF_INET, socket.SOCK_STREAM))
server.start()
