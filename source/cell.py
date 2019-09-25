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