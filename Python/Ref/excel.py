class ReadExcelSheet():

	def __init__(self, book, sheet):
		self.book = xlrd.open_workbook(book)
		self.sheet = self.book.sheet_by_name(sheet)

	def split(self, cell):
		letter_part = ''
		numeric_part = ''
		for each in cell:
			if each.isalpha() == True:
				letter_part += each
			elif each.isdigit() == True:
				numeric_part += each
		return [letter_part, int(numeric_part)]

	def num_col(self, cell):
		letter_part = self.split(cell)[0]
		numeric_col = 0
		exponent = 0
		for i in letter_part[::-1]:
			numeric_col += dictionaries.letter_order[i] * 26 ** exponent
			exponent += 1
		return int(numeric_col)

	def cell_value(self, cell):
		row = self.split(cell)[1]
		col = self.num_col(cell)
		cell_value = self.sheet.cell(row-1, col-1).value
		return cell_value

class WriteExcelSheet():

	def __init__(self, book, sheet):
		self.bookname = book
		self.book = xlwt.Workbook(self.bookname)
		self.sheet = self.book.add_sheet(sheet)

	def split(self, cell):
		letter_part = ''
		numeric_part = ''
		for each in cell:
			if each.isalpha() == True:
				letter_part += each
			elif each.isdigit() == True:
				numeric_part += each
		return [letter_part, int(numeric_part)]

	def num_col(self, cell):
		letter_part = self.split(cell)[0]
		numeric_col = 0
		exponent = 0
		for i in letter_part[::-1]:
			numeric_col += dictionaries.letter_order[i] * 26 ** exponent
			exponent += 1
		return int(numeric_col)

	def write(self, cell, value):
		row = self.split(cell)[1]
		col = self.num_col(cell)
		self.sheet.write(row-1, col-1, value)

	def save(self):
		self.book.save(self.bookname)