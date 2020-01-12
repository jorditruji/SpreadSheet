import string
from src.cells import CellFactory
from src.utils.utils import utils
from src.exceptions import AliasNotFound, CellNotFound, PathNotFound, CopyAlias
import pickle
from os import path
from src.expression_parser.parser import Parser


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
		self.parser = Parser()

	def set(self, alias, value):
		"""
		Set values of the cell by cell alias

		Args:
			alias (str): Alias of cell
			value (any): Value to set

		"""
		# Parse alias
		position = utils.parse_alias(alias=alias)
		if position['col'] not in self.columns_alias:
			raise AliasNotFound(col=position['col'])
		if position['row'] > self.max_rows:
			raise AliasNotFound(row=position['row'])

		# Parse value
		type = utils.infer_cell_type(value=value)
		params = {
			"alias": alias,
			"value": value
		}

		# Patch to evaluate propperly absolute values
		# It doesn't matter when evaluating if its an absolute or not column or row.
		# It just makes sense in copy_cells
		value = value.replace('$', '')

		# Expression cells should be created once they are parsed
		if type == 'ExpressionCell':
			# Check for ranges:
			ranges = utils.find_ranges(value)
			for _range in ranges:
				new_str = utils.from_range_to_str(_range, self.columns_alias)
				# Replace A1:A3 for A1,A2, A3
				value = value.replace(_range, new_str)

			params['expression'] = self.parser.parse(value[1:])# = char is messing the parser

			cell = self.cell_factory.create_cell(type=type, params=params)
			# Once we have created the cell ww will evaluate its expression and update its value
			involved_cells_alias = cell.expression.variables()
			value_dict = {}
			for alias in involved_cells_alias:
					value_dict[alias] = self.get_cell(alias)[0].get_value()

			cell.update_value(value_dict)
		else: 
			cell = self.cell_factory.create_cell(type=type, params=params)
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

	def update_cell(self, alias, value):
		"""
		Updates every a concrete cell
		Returns:
			boolean: Success
		"""
		
		cell_2_update, idx = self.get_cell(alias)
		new_type = utils.infer_cell_type(value=value)
		# Updating cells without changing its type
		if new_type == cell_2_update.type:

			if new_type == 'expression':
				cell_2_update.expression = self.parser.parse(value[1:])
				involved_cells_alias = cell_2_update.expression.variables()
				value_dict = {}
				for alias in involved_cells_alias:
					value_dict[alias] = self.get_cell(alias)[0].value
				cell.update_value(value_dict)				

			else:
				cell_2_update.update_value(value)
		else:
			# If the type is different we just recreate the cell
			self.remove_cell(alias)
			self.set(alias, value)

	def copy_cell(self, alias_origin, range):
		"""
		Copy the the type of the cell and adapts to the destination cell
		Args:
			alias_origin (str): Alias of the cell to be copied
			range (str): Alias of cell or cells to be set


		"""
		# TODO: Handle Exceptions!!!!!!!!
		# Get cell origin information
		position_origin = utils.parse_alias(alias=alias_origin)
		cell_origin, _ = self.get_cell(alias=alias_origin)

		involved_cells_origin = utils.find_cells(cell_origin.string_expression)

		# Convert range (if its) to list of alias
		if ":" in range:
			alias_list = utils.from_range_to_list(range_=range, letter_list=self.columns_alias)
		else:
			alias_list = [range]

		for alias in alias_list:

			# Extract column and row of destination
			position_dest = utils.parse_alias(alias=alias)

			# Get column index in alias information list
			indx_col_origin = self.columns_alias.index(position_origin['col'])
			indx_col_dest = self.columns_alias.index(position_dest['col'])

			# Calculate differences between origin and destination
			difference_col = indx_col_dest - indx_col_origin
			difference_row = position_dest['row'] - position_origin['row']

			string_expression = cell_origin.string_expression
			expression_parts = []

			for i, cell in enumerate(involved_cells_origin):

				absolutes = cell.count('$')
				if absolutes == 0:
					# For each involved cell alias, parse position and calculate new alias
					tmp_position = utils.parse_alias(alias=cell)
					new_col_indx = int(self.columns_alias.index(tmp_position['col'])) + difference_col
					new_row = tmp_position['row'] + difference_row
					new_col = self.columns_alias[new_col_indx]

					# New alias to be set in the string expression
					new_alias = "{}{}".format(new_col, new_row)

					if new_row <= 0 or new_col_indx < 0:
						raise CopyAlias(alias_origin=cell, alias_dest=new_alias)

				elif absolutes == 1:
					index_abs = cell.index('$')
					aux_cell = cell.replace('$', '')
					tmp_position = utils.parse_alias(alias=aux_cell)
					if index_abs == 0:
						new_col = "${}".format(tmp_position['col'])
						new_row = tmp_position['row'] + difference_row
					else:
						new_col_indx = int(self.columns_alias.index(tmp_position['col'])) + difference_col
						new_row = "${}".format(tmp_position['row'])
						new_col = self.columns_alias[new_col_indx]

					# New alias to be set in the string expression
					new_alias = "{}{}".format(new_col, new_row)

					if new_row <= 0 or new_col_indx < 0:
						raise CopyAlias(alias_origin=cell, alias_dest=new_alias)

				elif absolutes == 2:
					new_alias = cell


				# Replace first alias found in string expression
				string_expression = string_expression.replace(cell, new_alias, 1)

				# Find finishing index for character treated, store it to rejoin later
				index = string_expression.index(new_alias) + len(new_alias)
				expression_parts.append(string_expression[:index])

				# Cut the changing string expression to not substitute replaced values.
				# Everything is done in same order
				string_expression = string_expression[index:]

			# Append residual parts of string expression.
			expression_parts.append(string_expression)
			new_string_expression = ''.join(expression_parts)
			try:
				self.set(alias=alias, value=new_string_expression)
			except Exception as e:
				print(e.custom_message)












