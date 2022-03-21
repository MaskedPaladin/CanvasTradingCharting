import canvas
import chart
import sys
import os

def mainMenu():
	option = input("1) Load chart from csv\n8) Exit\n> ") or None
	if option == "1":
		loadMenu()
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
	except:
		loadMenu()		
def showChart(path, candles, zoomFactor):
	data = chart.loadFromMtCsv(str(path))
	if candles != None:
		toDraw = data[len(data) - candles:]
	else:
		toDraw = data
	cv = canvas.Canvas(len(toDraw), chart.getMax(toDraw))
	cv.update(chart.getTilesByPoints(toDraw, zoomFactor))
	cv.drawCanvas()

	print("Open", "Close", "High", "Low")
	for value in toDraw:
		if value[0] > value[1]:
			print("\033[0;0;31m"+ str(value[0]), str(value[1]), str(value[2]), str(value[3]))
		elif value[0] < value[1]:
			print("\033[0;0;32m" + str(value[0]),  str(value[1]), str(value[2]), str(value[3]))
		elif value[0] == value[1]:
			print("\033[0;0;0m" + str(value[0]), str(value[1]), str(value[2]),  str(value[3]))
	print("\033[0;0;0m")
def main():
	while True:
		mainMenu()

main()
