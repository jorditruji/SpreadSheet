from .cell import Cell


class TextCell(Cell):
    """
    Holds the additional content for text cells

    Attributes:
        value (int, float): Cell value
        alias (str): Alias for the cell

    """

    def __init__(self, value, alias):
        super().__init__(alias=alias)
        self.type = 'text'
        self.value = value

