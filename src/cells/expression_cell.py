from .cell import Cell


class ExpressionCell(Cell):
    """
    Holds the additional content for expression cells

    Attributes:
        value (int, float): Cell value
        position (tupple): Position (col, row) of the cell
        alias (str): Alias for the cell
        expression (str): String expression for the cell

    """

    supported_expressions = [
        "SUMA",
        "MIN",
        "MAX",
        "PROMEDIO"
    ]

    def __init__(self, value, position, alias, expresion):
        super().__init__(position=position, alias=alias)
        self.type = 'expression'
        self.expression = expresion
        self.value = value


