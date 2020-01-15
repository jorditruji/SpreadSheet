from .cell import Cell


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
        self.expression = params['expression']
        self.string_expression = params['value']
        self.value = None
        self.value_dict = {}

    def printify(self):
        print('=================GET CELL====================')
        print('CELL: {}'.format(self.alias))
        print('TYPE: {}'.format(self.type.upper()))
        print('VALUE: {}'.format(self.value))
        print('EXPRESSION: {}'.format(self.string_expression))
        #printer = self.expression.prettyprint()
        #print(printer)
        print(vars(self))
        print('\n')

    def update_value(self,new_variable_dict):
        try:
            self.value_dict.update(new_variable_dict)
            self.value = self.expression.evaluate(self.value_dict)
            self.notify()

        except Exception as e:
            raise e





