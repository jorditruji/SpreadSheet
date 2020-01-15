from .subject import Subject



class Cell(Subject):
	"""
	Holds the basic content of a cell.

	Attributes:
		alias (str): Alias for the cell


	"""


	def __init__(self, alias=None):
		super().__init__()
		self.alias = alias
		self._observers = list()


	def get_value(self):
		return self.value

	def attach(self, observer):
		"""
		Attach an observer to the subject.
		"""
		self._observers.append(observer)
		

	def detach(self, observer):
		"""
		Detach an observer from the subject.
		"""
		self._observers.remove(observer)

	
	def notify(self):
		"""
		Notify all observers about an event.
		"""
		for cell in self._observers:
			print({self.alias:self.value})
			print("Updating cell by subscription \n\n\n\n\n\n")
			value_dict = {}
			value_dict[self.alias] = self.value
			cell.update_value(value_dict)


cell = Cell

