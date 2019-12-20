from src.operations import MEAN, MAX, MIN, SUM
from . import ExcelParser

class ExpressionParser(object):
    """
    Provides the needed methods in order to find out which cells are involved in an action and also perform operations
    on them if needed

    Attributes:
        operations (tupple): Names for the possible operations.
        operation_lambda (dict): Operation lambda definition for the possible operations.

    """
    def __init__(self):
        self.operations = ("SUMA", "MIN", "MAX", "PROMEDIO")  # Parenthesis required for further use in regexps
        self.operation_lambda = {
            "SUMA": SUM.do,
            "MIN": MIN.do,
            "MAX": MAX.do,
            "PROMEDIO": MEAN.do

        }
        self.cells_values = []

    @classmethod
    def parse_operation(cls, expression):
        """
        Parses string expressions and returns the operation found as a function.

        Args:
            expression (str): Cell expression (i.e SUMA(A1:A22))

        Returns:
            function: Function which implements the detected operation in expression.

        """


    @classmethod
    def parse_value_cell(cls, value):
        """
        Parses input value
        Args:
            value (str): String or numeric value

        Returns:
            tupple: (type of cell, expression if applies).
        """

        type = 'TextCell'
        if value.isdigit():
            type = 'NumericCell'

        # Expressions should start with =
        if value[0] == '=':
            type = 'ExpressionCell'

            return type
        return type

    @classmethod
    def parse_alias(cls, alias):
        """
        Parses cell alias
        Args:
            alias (str): Cell alias

        Returns:
            dict: col, row
        """
        col = ''
        row = ''
        for c in alias:
            if c.isdigit():
                row += c
            else:
                col += c

        return {
            "col": col,
            "row": int(row)
        }

    @classmethod
    def from_range_to_list(cls, range_, letter_list):
        """
        Converts range (A1:A6) to list of alias
        Args:
            range_ (str): Range of cells
            letter_list (list): Liat of possible column alias

        Returns:
            list: list of cell alias involved
        """

        range_list = range_.split(':')
        min_range = cls.parse_alias(alias=range_list[0])
        max_range = cls.parse_alias(alias=range_list[1])

        alias_list = []
        init = int(min_range['row'])
        fin = int(max_range['row']) + 1
        list_rows = range(init, fin)
        for i in list_rows:
            alias_list.append('{}{}'.format(min_range['col'], i))

        return alias_list

