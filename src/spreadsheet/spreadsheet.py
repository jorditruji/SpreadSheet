import string
from src.cells import Cell, ExpressionCell, NumericCell, TextCell
from src.expression_parser import expression_parser
from src.exceptions import AliasNotFound, CellNotFound


class SpreadSheet:
	"""
	This is the main class that will contain all the Cells and Expressions making a SpreadSheet.
	All the functions contained in the menu, should be executed here.

	Holds a maximum of 702 columns (from A to ZZ) even though it can be easily expanded
	"""

	def __init__(self):

		# Contains column alias to make it easier to evaluate expression
		self.columns_alias = self.__make_column_alias()

		self.cell_maker = {
			"text": TextCell,
			"numeric": NumericCell,
			"expression": ExpressionCell
		}

		self.cells = []
		self.max_rows = 100

	def set(self, alias, value):
		"""
		Set values of the cell by cell alias

		Args:
			alias (str): Alias of cell
			value (any): Value to set

		"""
		# Parse alias
		position = expression_parser.ExpressionParser.parse_alias(alias=alias)
		if position['col'] not in self.columns_alias:
			raise AliasNotFound(col=position['col'])
		if position['row'] > self.max_rows:
			raise AliasNotFound(row=position['row'])

		# Parse value
		type, expression = expression_parser.ExpressionParser.parse_value_cell(value=value)
		params = {
			"alias": alias,
			"value": value,
			"expression": expression
		}
		cell = self.cell_maker[type](params=params)
		self.cells.append(cell)

	def get_cell(self, alias):
		"""
		Get a Cell object by its alias

		Args:
			alias (str): Alias of cell

		Returns:
			Cell: The Cell object itself

		"""
		for cell in self.cells:
			if cell.alias == alias:
				return cell

		raise CellNotFound(alias=alias)


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
		return letters

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


