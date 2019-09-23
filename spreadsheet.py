import numpy as np
import re
import string
import itertools


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

	def __init__(self, alias_list, expression = None):
		if expression is not None:
			assert expression[0] == '='
			assert expression.count('(') == expression.count(')') == 1
		self.alias_list = alias_list
		self.expression = expression
		self.operations = ("(SUMA)", "(MIN)", "(MAX)", "(PROMEDIO)")
		self.operation_lambda = {
			"SUMA": (lambda x,y : x + y )

		}


	def set_expression(self, expression):
		# Set expression a value
		assert expression[0] == '='
		assert expression.count('(') == expression.count(')') == 1		
		self.expression = expression


	def parse_expression(self):
		# Check amount of operators
		operations = [re.findall(operation, self.expression) for operation in self.operations]
		#Clean empty matches
		operations = [operation[0] for operation in operations if operation]
		n_operations = len(operations)

		# Check if the formula is correct
		if n_operations>1:
			raise ValueError("Chaining different operators is not implemented.")
		elif n_operations==0:
			raise ValueError("Formula is not valid")
		else:
			# Get operation
			operation = operations[0]

			# Find whichs cells do we need for the formulae
			involved_cells_str = re.search(r'\((.*?)\)',self.expression).group(1)
			involved_idxs = []

			# Iterate over groups (; is just separation)
			for group in involved_cells_str.split(';'):
				# Check if it is an slice
				if ':' in group:
					init, end = group.split(':')
					print(init, end)
					# Extract column alias
					init_column = "".join(re.findall("[a-zA-Z]+", init))
					end_column = "".join(re.findall("[a-zA-Z]+", end))

					# Extract row idx, as python array starts at poisition 0 we need to substract one to the row idxs

					init_row = int(''.join([char for char in init if char not in init_column]))-1
					end_row = int(''.join([char for char in end if char not in end_column]))-1
					print("Start: {}\n End {}\n".format((init_column, init_row),(end_column, end_row)))


					# Convert alias to idx for columns
					init_column, end_column = self.code_2_idx(init_column, end_column)

					print("Start: {}\n End {}\n".format((init_column, init_row),(end_column, end_row)))

					range_rows  = list(range(init_row, end_row+1, 1))
					range_cols = list(range(init_column, end_column+1, 1))
					print(range_rows)
					for position in itertools.product(range_cols, range_rows):
						involved_idxs.append(position)

				else:
					col = "".join(re.findall("[a-zA-Z]+", group))
					row = int("".join([char for char in group if char not in col]))-1
					involved_idxs.append((self.alias_list.index(col), row))

			return operation, involved_idxs


	def code_2_idx(self, init, end):

		return self.alias_list.index(init), self.alias_list.index(end)


class SpreadSheet:
	# Holds a maximum of 702 columns (from A to ZZ)
	def __init__(self, size):

		# Sizes of the spreadsheet
		self.n_rows = size[0]
		self.n_cols = size[1]

		# Contains solumn alias to make it easier to evaluate expression
		self.columns_alias = self.make_column_alias()

		self.expression_handler = Expression(self.columns_alias)

		# Initalize grip with empty cell objects
		self.matrix = np.empty((self.n_cols, self.n_rows), dtype = object)
		self.matrix[:] = Cell()

	def set(self, posx, posy, value):
		# Set values of the cell by coordinates
		self.matrix[posx, posy] = Cell(value=value) 


	def get_by_pos(self, posx, posy):
		# Get the values of a cell by its position
		type_ = self.matrix[posx, posy].get_type()
		print(type_)
		if type_ == 'formulae':
			self.expression_handler.set_expression(self.matrix[posx, posy].value)
			operation, involved_idxs = self.expression_handler.parse_expression()
			print(involved_idxs)
			involved_values = [self.matrix[posx, posy].value for posx, posy in involved_idxs]
			print(involved_values)


		else:
			print(posx, posy)
			return self.matrix[posx, posy]

	def make_column_alias(self):
		# Prepare alias of the columns (A,B,C..ZZ)
		# a to z
		letters = list(string.ascii_lowercase.upper())
		# aa to zz
		letters.extend([(i+b).upper() for i in letters for b in letters])

		# limit to n_cols
		return letters[0:self.n_cols]




if __name__ == '__main__':
	excel = SpreadSheet([20,20])
	print(str(excel))
	excel.set(0,0, 'eric')
	print(excel.get_by_pos(0,0).value)
	excel.set(0, 1, 10)
	excel.set(0, 2, 10)
	print(excel.get_by_pos(0,2).value)
	print(excel.matrix)
	excel.set(0,3, "=SUMA(A2:A3)")


	print(excel.get_by_pos(0,1).value)
	print(excel.get_by_pos(0,2).value)
	excel.get_by_pos(0,3)

	'''
	print(excel.get_by_pos(0,0).value)
	print(excel.columns_alias)
	expression_test = "=PROMEDIO(AA1:BA3)"
	expression = Expression(excel.columns_alias, expression_test)
	operation, involved_idxs = expression.parse_expression()

	print(operation, involved_idxs)

	expression_test = "=PROMEDIO(A3;B3)"
	expression = Expression(excel.columns_alias, expression_test)
	operation, involved_idxs = expression.parse_expression()
	print(operation, involved_idxs)
	'''