import numpy as np
import re
import string

class Cell(object):
	""" Holds the content of a cell"""
	def __init__(self, value = None):

		self.value = value

	def get_type(self):
		if self.value is None:
			return "Empty"
		variable_type = type(self.value)
		if variable_type in (float, int):
			return "numeric"
		elif variable_type == str:
			if self.value[0] == '=':
				return "formulae"
			else:
				return "text"
		else:
			raise TypeError("Valid types are numeric, text and formula")


class Expression(Cell):
	def __init__(self, expression):
		assert expression[0] == '='
		assert expression.count('(') == expression.count(')') == 1
		self.expression = expression
		self.operations = ("(SUMA)", "(MIN)", "(MAX)", "(PROMEDIO)")

	def parse_expression(self):
		# Check amount of operators
		operations = [re.findall(operation, self.expression) for operation in self.operations]
		#Clean empty matches
		operations = [operation[0] for operation in operations if operation]
		n_operations = len(operations)
		if n_operations>1:
			raise ValueError("Chaining different operators is not implemented.")
		elif n_operations==0:
			raise ValueError("Formula is no valid")
		else:
			operation = operations[0]
			involved_cells_str = re.search(r'\((.*?)\)',self.expression).group(1)
			involved_idxs = []
			for group in involved_cells_str.split(';'):
				for elem 


	def code_2_idx(self, code):
		pass


class SpreadSheet:
	# Holds a maximum of 702 columns (from A to ZZ)
	def __init__(self, size):
		self.n_rows = size[0]
		self.n_cols = size[1]
		self.columns_alias = self.make_column_alias()
		self.matrix = np.empty((self.n_cols, self.n_rows), dtype = object)
		self.matrix[:] = Cell()

	def set(self, posx, posy, value):
		self.matrix[posx, posy].value = value 

	def get_by_pos(self, posx, posy):
		return self.matrix[posx, posy]

	def make_column_alias(self):
		# a to z
		letters = list(string.ascii_lowercase)
		# aa to zz
		letters.extend([i+b for i in letters for b in letters])

		# limit to n_cols
		return letters[0:self.n_cols]

if __name__ == '__main__':
	excel = SpreadSheet([20,20])
	print(str(excel))
	excel.set(0,0, 'eric')
	print(excel.get(0,0).value)

	expression_test = "=PROMEDIO(A1:B3)"
	expression = Expression(expression_test)
	expression.parse_expression()
