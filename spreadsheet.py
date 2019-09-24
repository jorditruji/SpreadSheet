import numpy as np
import string
from cell import Cell
from expression import Expression


class SpreadSheet:
	"""
	This is the main class that will contain all the Cells and Expressions making a SpreadSheet.
	All the functions contained in the menu, should be executed here.

	Holds a maximum of 702 columns (from A to ZZ)
	"""

	def __init__(self, size):

		# Sizes of the spreadsheet
		self.n_rows = size[0]
		self.n_cols = size[1]

		# Contains column alias to make it easier to evaluate expression
		self.columns_alias = self.make_column_alias()

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
			Cell: The Cell

		"""
		type_ = self.matrix[posx, posy].get_type()
		#print(type_)
		if type_ == 'formulae':
			self.expression_handler.set_expression(self.matrix[posx, posy].value)
			operation, involved_idxs = self.expression_handler.parse_expression()
			#print(involved_idxs)
			involved_values = [self.matrix[posx, posy].value for posx, posy in involved_idxs]
			#print(involved_values)


		else:
			#print(posx, posy)
			return self.matrix[posx, posy]

	def make_column_alias(self):
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
	excel.set(0, 0, 'eric')
	print(excel.get_by_pos(0, 0).value)
	excel.set(0, 1, 10)
	excel.set(0, 2, 10)
	print(excel.get_by_pos(0, 2).value)
	print(excel.matrix)
	excel.set(0, 3, "=SUMA(A2:A3)")

	print(excel.get_by_pos(0, 1).value)
	print(excel.get_by_pos(0, 2).value)
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
