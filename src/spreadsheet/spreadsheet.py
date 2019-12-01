import string
from src.cells import Cell
from src.expression_parser import expression_parser

class SpreadSheet:
	"""
	This is the main class that will contain all the Cells and Expressions making a SpreadSheet.
	All the functions contained in the menu, should be executed here.

	Holds a maximum of 702 columns (from A to ZZ) even though it can be easily expanded
	"""

	def __init__(self, size=[5, 5]):

		# Sizes of the spreadsheet
		self.n_rows = size[0]
		self.n_cols = size[1]

		# Contains column alias to make it easier to evaluate expression
		self.columns_alias = self.__make_column_alias()

		self.cells = []
		row = 1
		for i in range(1, self.n_cols):
			cell = Cell(position=(i, row), alias=self.columns_alias[i])
			self.cells.append(cell)

	def set(self, posx, posy, value):
		"""
		Set values of the cell by coordinates

		Args:
			posx (int): Index position for column
			posy (int): Index position for row
			value(any): Value to set

		"""
		pass

	def get_value_by_pos(self, posx, posy):
		"""
		Get a Cell value by its position

		Args:
			posx (int): Index position for column
			posy (int): Index position for row

		Returns:
			Cell: The Cell value

		"""
		pass

	def get_cell_by_pos(self, posx, posy):
		"""
		Get a Cell object by its position

		Args:
			posx (int): Index position for column
			posy (int): Index position for row

		Returns:
			Cell: The Cell object itself

		"""
		pass

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

	def evaluate_expression(self, cell):
		"""
		Parses string cell expression and returns the value.
		Args:
			cell (ExpressionCell): cell to be evaluated

		Returns:
			float: value for expression
		"""
		pass

	def copy_cell(self, alias_origin, alias_dest):
		"""
		Copy the the type of the cell and adapts to the destination cell
		Args:
			alias_origin (str): Alias of the cell to be copied
			alias_dest (str): Alias of cell to be set

		Returns:
			Cell: cell destinnation with coppied contents and adapted as the specifications

		"""
		pass


spreadsheet = SpreadSheet()
