from .cell import Cell


class ExpressionCell(Cell):
    """
    Holds the additional content for expression cells

    Attributes:
        value (int, float): Cell value
        alias (str): Alias for the cell
        expression (str): String expression for the cell

    """

    supported_expressions = [
        "SUMA",
        "MIN",
        "MAX",
        "PROMEDIO"
    ]

    def __init__(self, value, alias, expresion):
        super().__init__(alias=alias)
        self.type = 'expression'
        self.expression = expresion
        self.value = value


