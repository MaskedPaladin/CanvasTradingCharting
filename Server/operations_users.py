class Operation:
	def __init__(self, identity, price, symbol):
		self.identity = identity
		self.price= price
		self.symbol = symbol
	def show(self):
		print("==========Operations==========")
		print("|id|", self.identity, "|price", self.price, "|symbol", self.symbol,"|")
class User:
	def __init__(self, identity, money):
		self.identity = identity
		self.money = money
		self.operations = []
	def buyOperation(self, operation):
		self.money-=operation.price
		self.operations.append(operation)
	def sellOperation(self, operation):
		for i, op in enumerate(self.operations):
			if op == operation:
				self.money+=op.price
				self.operations.pop(i)
	def show(self):
		print("==========User==========")
		print("|id", self.identity, "|money", self.money,"|")
		for element in self.operations:
			element.show()
def getActualPrice(arrayData):
	return arrayData[len(arrayData)-1]

def buyOperation(user, operation):
	if user.money < operation.price:
		print("Not enough money")
	else:
		user.buyOperation(operation)
def sellOperation(user, operation):
	for op in user.operations:
		if op == operation:
			user.sellOperation(operation)
			break

u = User(0, 2000)

buyOperation(u, Operation(0, 12, "AMD"))
sellOperation(u, u.operations[0])

u.show()
