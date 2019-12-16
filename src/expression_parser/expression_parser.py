from src.operations import MEAN, MAX, MIN, SUM


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



    @classmethod
    def parse_locations(cls, alias):
        """
        Converts SpreadSheet alias into cell coordinates.

        Args:
            alias (str): Cell or cells alias (i.e A1:A12)

        Returns:
            list: Positions in a list of tupples (pos_x, pos_y)

        """
        pass

    @classmethod
    def parse_operation(cls, expression):
        """
        Parses string expressions and returns the operation found as a function.

        Args:
            expression (str): Cell expression (i.e SUMA(A1:A22))

        Returns:
            function: Function which implements the detected operation in expression.

        """
        pass

    @classmethod
    def parse_value_cell(cls, value):
        """
        Parses input value
        Args:
            value (str): String or numeric value

        Returns:
            str: type of cell.
        """

        type = 'text'
        if value.isdigit():
            type = 'numeric'

        # TODO: type expression to be done
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





