import random
import canvas as c

#Open, High, Low, Close
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
		values.append((float(data[1]), float(data[2]), float(data[3]), float(data[4])))
	return values
def getMax(array):
	max_value = 0
	for entry in array:
		if max(entry) > max_value:
			max_value = max(entry)
	return max_value

def getTilesByPoints(dataArray):
	tiles = []
	for i, entry in enumerate(dataArray):
		for n in range(int(round(entry[2])), int(round(entry[1]))):
			if entry[0] > entry[3]:
				if n not in range(int(round(entry[3])), int(round(entry[0]))):
					tiles.append((i, 0-n, "\033[0;0;0m|"))
				else:	
					tiles.append((i, 0-n, "\033[0;0;41m "))
			elif entry[0] < entry[3]:
				if n not in range(int(round(entry[0])), int(round(entry[3]))):
					tiles.append((i, 0-n, "\033[0;0;0m|"))
				else:	
					tiles.append((i, 0-n, "\033[0;0;42m "))
			elif entry[0] == entry[3]:
				tiles.append((i, 0-n, "\033[0;0;0m|"))
	return tiles
