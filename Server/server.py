import threading
import socket
import server_data_api as sda
import sys
import logging
class ThreadedTcpSocketServer(threading.Thread):
	def __init__(self, ip, port, socket):
		threading.Thread.__init__(self)
		self.ip = ip
		self.port = port
		self.socket = socket
	def run(self):
		try:
			
			self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
			self.socket.bind((self.ip, self.port))
			self.socket.listen()
			while True:
				connection, ip = self.socket.accept()
				data = connection.recv(1024)
				encoded = str(data, encoding="utf-8")
				print(encoded)
				command = encoded.split(",")
				if command[0] == "05":
					connection.send(sda.loadUser(command[1], command[2]).encode("utf-8"))
				elif command[0] == "06":
					connection.send(sda.insertUser(command[1], command[2], command[3]).encode("utf-8"))
				elif encoded == str("09"):
					files = sda.getAllCsv()
					for f in files:
						print(f)
						data = f.read()
						connection.send(data)
						f.close()
					connection.send("21")
		except Exception as e:
			logging.exception(">")
			raise
			sys.exit()
server = ThreadedTcpSocketServer('localhost', 25565, socket.socket(socket.AF_INET, socket.SOCK_STREAM))
server.start()
server.join()
