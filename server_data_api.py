import os

def loadUser(login, password):
	fileClear()
	f = open("userdata", "r")
	lines = f.readlines()
	for l in lines:
		fields = l.split(",")
		if login == fields[0] and password == fields[1]:
			return "01" 
			f.close()
			break
	# 02 Code user dont exist and dont be loaded
	f.close()
	return "02"
def insertUser(login, password, money):	
	fileClear()
	f = open("userdata", "r")
	lines = f.readlines()
	for l in lines:
		fields = l.split(",")
		if fields[0] == login:
			# 03 Code user exists and cant create
			f.close()
			return "03"
	f.close()
	f = open("userdata", "a+", encoding="utf-8")
	f.write(str(login)+","+str(password)+","+str(money+"\n"))
	return "01"
	f.close()
def removeUser(login, password):
	fileClear()
	with open("userdata", "r") as r:
		d = r.readlines()
		with open("tmp", "w") as w:
			for line in d:
				fields = line.split(",")
				if fields[0] != login or fields[1] != password:
					w.write(fields[0]+","+fields[1]+","+fields[2]+"\n")
	os.replace("tmp", "userdata")
	return "02"
def fileClear():
	with open("userdata","r") as r:
		d = r.readlines()
		with open("tmp", "w") as w:
			for line in d:
				if line.strip()!="":
					w.write(line)
	os.replace("tmp", "userdata")
def showAll():
	fileClear()
	f = open("userdata", "r")
	lines = f.readlines()
	for l in lines:
		print("-------------------------------")
		print(l,end="")
		print("-------------------------------")
	f.close()
	return "01"
