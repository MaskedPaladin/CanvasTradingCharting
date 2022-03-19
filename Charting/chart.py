import canvas as c
import random

#Open, Close, High, Low
def simulate(candles):
	dataArray = []
	for i in range(candles):
		data = [random.randint(1, 20), random.randint(1, 20), random.randint(1, 20), random.randint(1, 20)]
		data[2] = random.randint(max(data), 20)
		data[3] = random.randint(1, min(data))
		if i > 0:
			data[0] = dataArray[i-1][1]	
		data = (data[0], data[1], max(data), min(data))
		dataArray.append(data)
	return dataArray

def loadFromMtCsv(path):
	values = []
	f = open(path, "r", encoding="utf-16-le")
	lines = f.readlines()
	for line in lines:
		data = line.split(",")
		values.append((int(float(data[1])), int(float(data[4])), int(float(data[2])), int(float(data[3]))))
	return values
def getMax(array):
	max_value = 0
	for entry in array:
		if max(entry) > max_value:
			max_value = max(entry)
	return max_value

def getTilesByPoints(dataArray):
	tiles = []
	for i, entry in enumerate(data):
		for n in range(entry[3], entry[2]):
			if entry[0] > entry[1]:
				if n not in range(entry[1], entry[0]):
					tiles.append(c.Tile(i, 0-n, 0, "\033[0;0;0m|"))
				else:	
					tiles.append(c.Tile(i, 0-n, 0, "\033[0;0;41m "))
			elif entry[0] < entry[1]:
				if n not in range(entry[0], entry[1]):
					tiles.append(c.Tile(i, 0-n, 0, "\033[0;0;0m|"))
				else:	
					tiles.append(c.Tile(i, 0-n, 0, "\033[0;0;42m "))
	return tiles
