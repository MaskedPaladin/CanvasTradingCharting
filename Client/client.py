import threading
import socket
import sys
from client import *
class ThreadedTcpSocketClient(threading.Thread):
	def __init__(self, ip, port):
		threading.Thread.__init__(self)
		self.ip = ip
		self.port = port
		self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	def send(self, content):
		self.socket.send(content)
	def recv(self, bufferSize):
		return self.socket.recv(bufferSize)
	def connect(self):
		self.socket.connect((self.ip, self.port))
	def close(self):
		self.socket.close()
def loginSend(ip, port, user, password):
	c = ThreadedTcpSocketClient(ip, port)
	c.start()
	c.connect()
	c.send(("05,"+user+","+password).encode("utf-8"))
	c.join()
	data = c.recv(1024)
	c.close()
	return data
def registerSend(ip, port, user, password, money):
	c = ThreadedTcpSocketClient(ip, port)
	c.start()
	c.connect()
	c.send(("06,"+user+","+password+","+money).encode("utf-8"))
	c.join()
	data = c.recv(1024)
	c.close()
	return data
