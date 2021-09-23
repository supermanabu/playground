def gcd(m,n):
	while m%n != 0:
		oldm = m
		oldn = n

		m = oldn
		n = oldm%oldn
	return n

class Fraction:

	def __init__(self, top, bottom):
		if type(top) != int or type(bottom) != int:
			raise RunTimeError('The numerator or the denominator must be an integer.')
		else:
			common = gcd(top, bottom)
			self.num = top//common
			self.den = bottom//common

	def __str__(self):
		common = gcd(self.num, self.den)
		return str(self.num) + "/" + str(self.den)

	def __add__(self, otherfraction):
		newnum = self.num * otherfraction.den + self.den * otherfraction.num
		newden = self.den * otherfraction.den

		return Fraction(newnum, newden)

	def __sub__(self, otherfraction):
		newnum = self.num * otherfraction.den - self.den * otherfraction.num
		newden = self.den * otherfraction.den

		return Fraction(newnum, newden)

	def __mul__(self, otherfraction):
		newnum = self.num * otherfraction.num
		newden = self.den * otherfraction.den

		return Fraction(newnum, newden)

	def __truediv__(self, otherfraction):
		newnum = self.num * otherfraction.den
		newden = self.den * otherfraction.num

		return Fraction(newnum, newden)

	def __gt__(self, otherfraction):
		newnum1 = self.num * otherfraction.den
		newnum2 = self.den * otherfraction.num
		return newnum1 > newnum2

	def __ge__(self, otherfraction):
		newnum1 = self.num * otherfraction.den
		newnum2 = self.den * otherfraction.num
		return newnum1 >= newnum2

	def __lt__(self, otherfraction):
		newnum1 = self.num * otherfraction.den
		newnum2 = self.den * otherfraction.num
		return newnum1 < newnum2

	def __le__(self, otherfraction):
		newnum1 = self.num * otherfraction.den
		newnum2 = self.den * otherfraction.num
		return newnum1 <= newnum2

	def __ne__(self, other):
		firstnum = self.num * other.den
		secondnum = other.num * self.den

		return firstnum != secondnum

	def __eq__(self, other):
		firstnum = self.num * other.den
		secondnum = other.num * self.den

		return firstnum == secondnum

	def getNum(self):
		return self.num

	def getDen(self):
		return self.den

f1 = Fraction(1,6)
f2 = Fraction(1,2)
a = 1
print(a.__repr__())