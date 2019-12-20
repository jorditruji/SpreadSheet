from .cell import Cell
from src.expression_parser import TokenExpression

class ExpressionCell(Cell):
    """
    Holds the additional content for expression cells

    Attributes:
        params (dict)

    """

    supported_expressions = [
        "SUMA",
        "MIN",
        "MAX",
        "PROMEDIO"
    ]

    def __init__(self, params):
        super().__init__(alias=params['alias'])
        self.type = 'expression'
        self.expression = TokenExpression(params['value'])
        self.string_expression = params['value']
        self.value = None

    def printify(self):
        print('=================GET CELL====================')
        print('CELL: {}'.format(self.alias))
        print('TYPE: {}'.format(self.type.upper()))
        print('VALUE: {}'.format(self.value))
        print('EXPRESSION: {}'.format(self.string_expression))
        printer = self.expression.prettyprint()
        print(printer)
        print('\n')





