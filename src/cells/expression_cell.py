from .cell import Cell


class ExpressionCell(Cell):

    supported_expressions = [
        "SUMA",
        "MIN",
        "MAX",
        "PROMEDIO"
    ]

    def __init__(self, expresion):
        self.type = 'expression'
        self.expression = expresion

