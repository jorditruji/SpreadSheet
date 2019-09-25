import re
import itertools
from cell import Cell
from statistics import mean 

class Expression(Cell):
	"""
	Handles the expression inserted in a cell.

	Attributes:
		alias_list (list): Ordered alias list for the columns in Spreadsheet.
		expression (str): Operation expression for the Cell. Default is None.
		operations (tupple): Names for the possible operations.
		operation_lambda (dict): Operation lambda definition for the possible operations.

	"""
	def __init__(self, alias_list, expression = None):
		if expression is not None:
			assert expression[0] == '='
			assert expression.count('(') == expression.count(')') == 1
		self.alias_list = alias_list
		self.expression = expression
		self.operations = ("(SUMA)", "(MIN)", "(MAX)", "(PROMEDIO)")
		self.operation_lambda = {
			"SUMA": (lambda x, y: x + y),
			"MIN": min,
			"MAX": max, 
			"PROMEDIO": mean

		}

	def set_expression(self, expression):
		"""
		Set expression a value

		Args:
			expression (str): Operation expression for a Cell.

		"""
		assert expression[0] == '='
		assert expression.count('(') == expression.count(')') == 1
		self.expression = expression

	def parse_expression(self):
		"""
		Parses operation expressions for a Cell to get the involved Cells to set its calculated value.

		Returns:
			lambda, list: The operation to be done, The list of index (col, row) for cells involved in the operation
		"""
		# Check amount of operators
		operations = [re.findall(operation, self.expression) for operation in self.operations]
		# Clean empty matches
		operations = [operation[0] for operation in operations if operation]
		n_operations = len(operations)

		# Check if the formula is correct
		if n_operations > 1:
			raise ValueError("Chaining different operators is not implemented.")

		# There is no operation at all
		elif n_operations == 0:
			raise ValueError("Formula is not valid")
		else:
			# Get operation
			operation = operations[0]

			# Find whichs cells do we need for the formulae
			involved_cells_str = re.search(r'\((.*?)\)', self.expression).group(1)
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
					init_column = self.code_2_idx(init_column)
					end_column = self.code_2_idx(end_column)

					print("Start: {}\n End {}\n".format((init_column, init_row),(end_column, end_row)))

					# Ranges on both axis
					range_rows  = list(range(init_row, end_row+1, 1))
					range_cols = list(range(init_column, end_column+1, 1))
					print(range_rows)
					# The total cells positions will be the cartesion product between x and y ranges
					for position in itertools.product(range_cols, range_rows):
						involved_idxs.append(position)

				# Not slice
				else:
					# Get the column alias and row number
					col = "".join(re.findall("[a-zA-Z]+", group))
					row = int("".join([char for char in group if char not in col]))-1
					# Append the position of the cell
					involved_idxs.append((self.alias_list.index(col), row))

			return self.operation_lambda[operation], involved_idxs

	def code_2_idx(self, alias):
		"""
		Get the index given an alias column

		Args:
			alias (str): Alias for a column

		Returns:
			int: Index for the column

		"""
		return self.alias_list.index(alias)