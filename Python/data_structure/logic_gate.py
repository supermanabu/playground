class LogicGate:

	def __init__(self, n):
		self.label = n
		self.output = None

	def getLabel(self):
		return self.label

	def getOutput(self):
		self.output = self.performGateLogic()
		return self.output

	def setNextPin(self, source):
		if self.pinA == None:
			self.pinA = source
		else:
			if self.pinB == None:
				self.pinB = source
			else:
				raise RunTimeError("Error: NO EMPTY PINS")

class BinaryGate(LogicGate):

	def __init__(self, n):
		super().__init__(n)

		self.pinA = None
		self.pinB = None

	def getPinA(self):
		if self.pinA == None:
			return int(input("Enter Pin A input for gate " + \
								self.getLabel() + "-->"))
		else:
			return self.pinA.getFrom().getOutput()

	def getPinB(self):
		if self.pinB == None:
			return int(input("Enter Pin B input for gate " + \
								self.getLabel() + "-->"))
		else:
			return self.pinB.getFrom().getOutput()

class UnaryGate(LogicGate):

	def __init__(self, n):
		super().__init__(n)

		self.pinA = None

	def getPinA(self):
		if self.pinA == None:
			return int(input("Enter Pin input for gate " + \
								self.getLabel() + "-->"))
		else:
			return self.pinA.getFrom().getOutput()

class AndGate(BinaryGate):

	def __init__(self, n):
		super().__init__(n)

	def performGateLogic(self):

		a = self.getPinA()
		b = self.getPinB()
		if a==1 and b==1:
			return 1
		else:
			return 0

class OrGate(BinaryGate):

	def __init__(self, n):
		super().__init__(n)

	def performGateLogic(self):

		a = self.getPinA()
		b = self.getPinB()
		if a==1 or b==1:
			return 1
		else:
			return 0

class NotGate(UnaryGate):

	def __init__(self, n):
		super().__init__(n)

	def performGateLogic(self):

		a = self.getPinA()
		if a==1:
			return 0
		else:
			return 1

class AndNotGate(BinaryGate):

	def __init__(self, n):
		super().__init__(n)

	def performGateLogic(self):

		g1 = AndGate('G1')
		g2 = NotGate('G2')
		c1 = Connector(g1, g2)
		return g2.getOutput()

class OrNotGate(BinaryGate):

	def __init__(self, n):
		super().__init__(n)

	def performGateLogic(self):

		g1 = OrGate('G1')
		g2 = NotGate('G2')
		c1 = Connector(g1, g2)
		return g2.getOutput()

class ExOrGate(BinaryGate):

	def __init__(self, n):
		super().__init__(n)

	def performGateLogic(self):

		a = self.getPinA()
		b = self.getPinB()
		if a!=b:
			return 1
		else:
			return 0

class HalfAdder(BinaryGate):

	def __init__(self, n):
		super().__init__(n)

	def performGateLogic(self):
		
		a = self.getPinA()
		b = self.getPinB()
		if a!=b:
			S = 1
		else:
			S = 0
		if a==1 and b==1:
			C = 1
		else:
			C = 0

		return str(C) + str(S)

class TernaryGate(LogicGate):

	def __init__(self, n):
		super().__init__(n)

		self.pinA = None
		self.pinB = None
		self.pinC = None

	def getPinA(self):
		if self.pinA == None:
			return int(input("Enter Pin A input for gate " + self.getLabel() + "-->"))
		else:
			return self.pinA.getFrom().getOutput()

	def getPinB(self):
		if self.pinB == None:
			return int(input("Enter Pin B input for gate " + self.getLabel() + "-->"))
		else:
			return self.pinB.getFrom().getOutput()

	def getPinC(self):
		if self.pinC == None:
			return int(input("Enter Pin C input for gate " + self.getLabel() + "-->"))
		else:
			return self.pinC.getFrom().getOutput()

class FullAdder(TernaryGate):

	def __init__(self, n):
		super().__init__(n)

	def performGateLogic(self):

		a = self.getPinA()
		b = self.getPinB()
		c = self.getPinC()
		abc = [a, b, c]
		if abc.count(1) == 0:
			C = 0
			S = 0
		elif abc.count(1) == 1:
			C = 0
			S = 1
		elif abc.count(1) == 2:
			C = 1
			S = 0
		elif abc.count(1) == 3:
			C = 1
			S = 1

		return str(C) + str(S)


class Connector:

	def __init__(self, fgate, tgate):
		self.fromgate = fgate
		self.togate = tgate

		tgate.setNextPin(self)

	def getFrom(self):
		return self.fromgate

	def getTo(self):
		return self.togate

g1 = AndGate("G1")
g2 = AndGate("G2")
g3 = OrGate("G3")
g4 = NotGate("G4")
c1 = Connector(g1, g3)
c2 = Connector(g2, g3)
c3 = Connector(g3, g4)

g5 = FullAdder('G5')
print(g5.getOutput())