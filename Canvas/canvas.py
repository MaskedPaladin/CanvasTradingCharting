import os, time

class Canvas:
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.canvas = [["\033[0;0;0m " for y in range(self.y)] for x in range(self.x)]
	def drawCanvas(self):
		os.system("clear")
		for y in range(self.y):
			if y > 0:
				print("\033[0;0;0m ")
			for x in range(self.x):
				print(self.canvas[x][y], end="")
		print("\033[0;0;0m ")
	def putPoint(self, x, y, character):
		self.canvas[x][y] = character
	def clearPoint(self, x, y):
		self.canvas[x][y] = "\033[0;0;0m "
	def update(self, tileArray):
		zMax = 0
		positions = []
		for i, tile in enumerate(tileArray):
			position = (tile.posX, tile.posY, tile.zCoord)
			positions.append(position)
			if position in positions:
				positions.append(position)
				for position in positions:
					if position[2] > zMax:
						zMax = i
			self.putPoint(tileArray[zMax].posX, tileArray[zMax].posY, tileArray[zMax].char)
			self.putPoint(tile.posX, tile.posY, tile.char)

class Tile:
	def __init__(self, posX, posY, zCoord, char):
		self.posX = posX
		self.posY = posY
		self.zCoord = zCoord
		self.char = char

