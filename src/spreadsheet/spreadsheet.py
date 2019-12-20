import string
from src.cells import CellFactory
from src.expression_parser import expression_parser
from src.exceptions import AliasNotFound, CellNotFound, PathNotFound
import pickle
import os.path
from os import path


class SpreadSheet:
	"""
	This is the main class that will contain all the Cells and Expressions making a SpreadSheet.
	All the functions contained in the menu, should be executed here.

	Holds a maximum of 702 columns (from A to ZZ) even though it can be easily expanded
	"""

	def __init__(self):

		# Contains column alias to make it easier to evaluate expression
		self.columns_alias = self.__make_column_alias()
		self.cell_factory = CellFactory()
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
		type = expression_parser.ExpressionParser.parse_value_cell(value=value)
		params = {
			"alias": alias,
			"value": value
		}
		cell = self.cell_factory.create_cell(typ=type, params=params)
		self.cells.append(cell)

	def get_cell(self, alias):
		"""
		Get a Cell object by its alias

		Args:
			alias (str): Alias of cell

		Returns:
			Cell: The Cell object itself

		"""
		for indx, cell in enumerate(self.cells):
			if cell.alias == alias:
				return cell, indx

		raise CellNotFound(alias=alias)

	def remove_cell(self, alias):
		"""
		Removes cell from the list
		Args:
			alias (str): Cell alias
		"""
		try:
			_, indx = self.get_cell(alias)
			self.cells.pop(indx)
		except Exception as e:
			print(e.custom_message)

	def save(self, name, path_='resources/'):
		"""
		Save Spreadsheet class

		"""
		if path.exists(path_) is False:
			raise PathNotFound(path_)

		with open('{}{}.pkl'.format(path_, name), 'wb') as output:
			pickle.dump(self, output)

	@classmethod
	def load(cls, name):
		"""
		Load Spreadsheet class
		Args:
			name: Name of the file

		"""
		path_ = 'resources/'
		directory = '{}{}.pkl'.format(path_, name)
		if path.exists(directory) is False:
			raise PathNotFound(directory)

		with open(directory, 'rb') as input:
			spreadsheet = pickle.load(input)

		return spreadsheet

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

	def copy_cell(self, alias_origin, range):
		"""
		Copy the the type of the cell and adapts to the destination cell
		Args:
			alias_origin (str): Alias of the cell to be copied
			range (str): Alias of cell or cells to be set


		"""
		# TODO: Handle Exceptions!!!!!!!!
		# Get cell origin information
		position_origin = expression_parser.ExpressionParser.parse_alias(alias=alias_origin)
		cell_origin, _ = self.get_cell(alias=alias_origin)

		# Get expression origin tokens
		params = {
			"alias": cell_origin.alias,
			"value": cell_origin.expression.string_expression
		}


		# Convert range to list of alias
		alias_list = expression_parser.ExpressionParser.from_range_to_list(range_=range, letter_list=self.columns_alias)

		for alias in alias_list:

			# Extract column and row of destination
			position_dest = expression_parser.ExpressionParser.parse_alias(alias=alias)

			# Get column index in alias information list
			indx_col_origin = self.columns_alias.index(position_origin['col'])
			indx_col_dest = self.columns_alias.index(position_dest['col'])

			# Calculate differences between origin and destination
			difference_col = indx_col_dest - indx_col_origin
			difference_row = position_dest['row'] - position_origin['row']

			# Create temporal cell to handle new wxpression
			tmp_cell = self.cell_factory.create_cell(typ='ExpressionCell', params=params)
			tmp_cell.expression.parse(tmp_cell.expression.string_expression)

			# Change tokens with type operand and range
			for i, token in enumerate(tmp_cell.expression.get_tokens()):
				if token['tsubtype'] == 'range' and token['ttype'] == 'operand':
					alias_obj = expression_parser.ExpressionParser.parse_alias(alias=token['tvalue'])

					# Calculate new expression
					indx_col_calc = self.columns_alias.index(alias_obj['col']) + difference_col
					row_calc = alias_obj['row'] + difference_row
					col_calc = self.columns_alias[indx_col_calc]
					tmp_cell.expression.tokens.items[i].tvalue = "{}{}".format(col_calc, row_calc)

			# Render new expression
			new_string_expression = "={}".format(tmp_cell.expression.render())
			self.set(alias=alias, value=new_string_expression)








