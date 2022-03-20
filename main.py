import canvas
import chart
import sys

data = chart.loadFromMtCsv(str(sys.argv[1]))
if len(sys.argv) == 3:
	toDraw = data[len(data)-int(sys.argv[2]):]
elif len(sys.argv) == 2:
	toDraw = data
cv = canvas.Canvas(len(toDraw), chart.getMax(toDraw))

cv.update(chart.getTilesByPoints(toDraw))
cv.drawCanvas()
print("Open", "Close", "High", "Low")
for value in toDraw:
	if value[0] > value[1]:
		print("\033[0;0;31m"+ str(value[0]), str(value[1]), str(value[2]), str(value[3]))
	elif value[0] < value[1]:
		print("\033[0;0;32m" + str(value[0]),  str(value[1]), str(value[2]), str(value[3]))
	elif value[0] == value[1]:
		print("\033[0;0;0m" + str(value[0]), str(value[1]), str(value[2]),  str(value[3]))
