from server_data_api import *

def console():
	option = input("1)Load user\n2)Insert user\n3)Delete user\n4)Show all\n> ")
	if option == "1":
		user = input("User\n> ")
		password = input("Password\n> ")
		code = loadUser(user, password)
		print(code)
		if code=="01":
			print("User exists")
		else:
			print("user dont exists")
		console()
	elif option == "2":
		user = input("User\n> ")
		password = input("Password\n> ")
		money = input("Money\n> ")
		code = insertUser(user,password,money)
		if code=="01":
			print("User inserted")
		else:

			print("User cant be inserted")	
		console()
	elif option == "3":	
		user = input("User\n> ")
		password = input("Password\n> ")
		removeUser(user, password)
		console()
	elif option == "4":
		showAll()
		console()

def main():
	console()
main()
