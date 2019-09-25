import numpy as np
import string
from cell import Cell
from expression import Expression
from functools import reduce

class SpreadSheet:
	"""
	This is the main class that will contain all the Cells and Expressions making a SpreadSheet.
	All the functions contained in the menu, should be executed here.

	Holds a maximum of 702 columns (from A to ZZ) even though it can be easily expanded
	"""

	def __init__(self, size):

		# Sizes of the spreadsheet
		self.n_rows = size[0]
		self.n_cols = size[1]

		# Contains column alias to make it easier to evaluate expression
		self.columns_alias = self.__make_column_alias()

		self.expression_handler = Expression(self.columns_alias)

		# Initalize grip with empty cell objects
		self.matrix = np.empty((self.n_cols, self.n_rows), dtype=object)
		self.matrix[:] = Cell()

	def set(self, posx, posy, value):
		"""
		Set values of the cell by coordinates

		Args:
			posx (int): Index position for column
			posy (int): Index position for row

		"""
		self.matrix[posx, posy] = Cell(value=value)

	def get_by_pos(self, posx, posy):
		"""
		Get a Cell object by its position

		Args:
			posx (int): Index position for column
			posy (int): Index position for row

		Returns:
			Cell: The Cell value

		"""
		type_ = self.matrix[posx, posy].get_type()
		#print(type_)
		if type_ == 'formulae':
			# Pass the expression to the handler
			self.expression_handler.set_expression(self.matrix[posx, posy].value)

			# Parse the expression
			operation, involved_idxs = self.expression_handler.parse_expression()

			# Get the values of the cells involved on the formulae
			involved_values = [self.matrix[posx, posy].value for posx, posy in involved_idxs]

			# Make sure the types of the cells are the same
			involved_types = set([self.matrix[posx, posy].get_type() for posx, posy in involved_idxs])

			# Make sure all the cells are of the same type and none of them are empty
			if len(involved_types)>1:
				raise TypeError("All cells involved on a formula should be of the same type")

			if None in involved_types:
				raise TypeError("Empty cells can not be used on formula")

			# Perform operation of the data and return its result
			print('Involved values',involved_values)
			print("operation: ", operation)
			result = reduce(operation, involved_values)
			print("With result: ", result)
			return result


		else:
			#print(posx, posy)
			return self.matrix[posx, posy].value

	def __make_column_alias(self):
		"""
		Prepare alias for columns from A to ZZ (limited to the number of columns set in SpreadSheet)

		Returns:
			list: ordered list for the labels of the columns

		"""
		# a to z
		letters = list(string.ascii_lowercase.upper())
		# aa to zz
		letters.extend([(i + b).upper() for i in letters for b in letters])

		# limit to n_cols
		return letters[0:self.n_cols]





if __name__ == '__main__':
	excel = SpreadSheet([20, 20])
	print(str(excel))
	excel.set(0, 0, 1)
	print(excel.get_by_pos(0, 0))
	excel.set(0, 1, 5)
	excel.set(0, 2, 10)
	print(excel.get_by_pos(0, 2))
	excel.set(0, 3, "=PROMEDIO(A1:A3)")

	print(excel.get_by_pos(0, 1))
	print(excel.get_by_pos(0, 2))
	excel.get_by_pos(0, 3)

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
