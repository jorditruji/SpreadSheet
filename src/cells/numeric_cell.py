from .cell import Cell


class NumericCell(Cell):
    """
    Holds the additional content for numeric cells

    Attributes:
        value (int, float): Cell value
        position (tupple): Position (col, row) of the cell
        alias (str): Alias for the cell

    """
    def __init__(self, value, alias):
        super().__init__(alias=alias)
        self.type = 'numeric'
        self.value = float(value)

