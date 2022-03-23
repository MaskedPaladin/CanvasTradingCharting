import canvas
import chart
import sys
import os
import logging
import client
import socket

def mainMenu():
	option = input("1) Load chart from csv\n2) Connect to server\n8) Exit\n> ") or None
	if option == "1":
		loadMenu()
	elif option == "2":
		clientMenu()
	elif option == "8":
		sys.exit()
	elif option == None:
		mainMenu()
	else:
		mainMenu()
def loadMenu():
	try:
		files = os.listdir("csv")
		for i, f in enumerate(files):
			print(str(i)+"/"+str(f))
		option = input("Select file to load\n> ") or None	
		if option == None:
			loadMenu()
		elif int(option) not in range(len(files)):
			loadMenu()
		else:
			candles = input("Number of candles to chart from the end\n> ")
			zoomFactor = input("Set the zoom\n> ")
			if not candles:
				candles = None
			if not zoomFactor:
				zoomFactor = 1
			if candles:
				candles = int(candles)
			showChart("csv/"+files[int(option)], candles, int(zoomFactor))	
	except Exception as e:
		logging.exception("Error")
		loadMenu()
def clientMenu():
	c = client.ThreadedTcpSocketClient("localhost", 25565, socket.socket(socket.AF_INET, socket.SOCK_STREAM))
	c.start()
	option = input("1) Login\n2) Register\n> ")
	if option == "1":
		user = str(input("User> "))
		password = str(input("Password> "))
		toSend = ("05,"+user+","+password).encode("utf-8")
		c.send(toSend)
	if option == "2":
		user = str(input("User> "))
		password = str(input("Password> "))
		money = str(input("Money> "))
		toSend = ("06,"+user+","+password+","+money).encode("utf-8")
		c.send(toSend)
	c.join()
def showChart(path, candles, zoomFactor):
	data = chart.loadFromMtCsv(str(path))
	dataIntegers = []
	for entry in data:
		dataIntegers.append((int(entry[0]/zoomFactor), int(entry[1]/zoomFactor), int(entry[2]/zoomFactor), int(entry[3]/zoomFactor)))
	if candles != None:
		toDraw = dataIntegers[len(dataIntegers) - candles:]
	else:
		toDraw = dataIntegers
	cv = canvas.Canvas(len(toDraw), int(chart.getMax(toDraw)))
	cv.update(chart.getTilesByPoints(toDraw))
	cv.drawCanvas()
	print("Open", "Close", "High", "Low")
	for value in data[len(dataIntegers) - candles:]:
		if value[0] > value[1]:
			print("\033[0;0;31m("+ str(float(value[0]))+", ", str(float(value[1]))+", ", str(float(value[2]))+", ", str(float(value[3]))+")")
		elif value[0] < value[1]:
			print("\033[0;0;32m("+ str(float(value[0]))+", ", str(float(value[1]))+", ", str(float(value[2]))+", ", str(float(value[3]))+")")
		elif value[0] == value[1]:
			print("\033[0;0;0m("+ str(float(value[0]))+", ", str(float(value[1]))+", ", str(float(value[2]))+", ", str(float(value[3]))+")")
	print("\033[0;0;0m\n")
def main():
	while True:
		mainMenu()

main()
