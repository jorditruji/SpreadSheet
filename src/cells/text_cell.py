from .cell import Cell


class TextCell(Cell):
    """
    Holds the additional content for text cells

    Attributes:
        value (int, float): Cell value
        position (tupple): Position (col, row) of the cell
        alias (str): Alias for the cell

    """

    def __init__(self, value, position, alias):
        super().__init__(position=position, alias=alias)
        self.type = 'text'
        self.value = value

