

class Cell(object):
	"""
	Holds the basic content of a cell.

	Attributes:
		position (tupple): Position (col, row) of the cell
		alias (str): Alias for the cell


	"""
	def __init__(self, position=None, alias=None):
		self.position = position
		self.alias = alias

cell = Cell

