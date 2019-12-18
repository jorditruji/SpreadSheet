from .cell import Cell


class NumericCell(Cell):
    """
    Holds the additional content for numeric cells

    Attributes:
        value (int, float): Cell value
        position (tupple): Position (col, row) of the cell
        alias (str): Alias for the cell

    """
    def __init__(self, params):
        super().__init__(alias=params['alias'])
        self.type = 'numeric'
        self.value = float(params['value'])

    def printify(self):
        print('=================GET CELL====================')
        print('CELL: {}'.format(self.alias))
        print('TYPE: {}'.format(self.type.upper()))
        print('VALUE: {}'.format(self.value))
        print('\n')