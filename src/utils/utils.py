import re


class Utils(object):
    """
    Provides the needed methods in order to find out which cells are involved in an action and also perform operations
    on them if needed

    """

    @classmethod
    def infer_cell_type(cls, value):
        """
        Parses input value
        Args:
            value (str): String or numeric value

        Returns:
            type of cell
        """

        type = 'TextCell'
        tmp_value = value.replace('.', '')
        if tmp_value.isdigit():
            type = 'NumericCell'

        # Expressions should start with =
        if value[0] == '=':
            type = 'ExpressionCell'
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
        min_range = cls.parse_alias(alias=range_list[0].upper())
        max_range = cls.parse_alias(alias=range_list[1].upper())

        alias_list = []
        init_row = int(min_range['row'])
        fin_row = int(max_range['row']) + 1
        init_col = letter_list.index(min_range['col'])
        fin_col = letter_list.index(min_range['col']) + 1
        list_rows = range(init_row, fin_row)
        list_cols = range(init_col, fin_col)
        for col in list_cols:
            for row in list_rows:
                alias_list.append('{}{}'.format(letter_list[col], row))

        return alias_list


    @classmethod
    def from_range_to_str(cls, range_, letter_list):
        """
        Converts range (A1:A6) to string of alias
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
        init_row = int(min_range['row'])
        fin_row = int(max_range['row']) + 1
        init_col = letter_list.index(min_range['col'])
        fin_col = letter_list.index(max_range['col']) + 1
        list_rows = range(init_row, fin_row)
        list_cols = range(init_col, fin_col)
        for col in list_cols:
            for row in list_rows:
                alias_list.append('{}{}'.format(letter_list[col], row))

        return ','.join(alias_list)

    @classmethod
    def find_ranges(cls, expression):
        #Match for LettersNumber:LettersNumber
        pattern = '[a-zA-Z]+\\d+:[a-zA-Z]+\\d+'# Find the pattern of ranges.
        return re.findall(pattern, expression)

    @classmethod
    def find_cells(cls, expression):
        # Match for LettersNumber:LettersNumber
        # supporting absolute and relative values.

        pattern = '[$a-zA-Z]+[$\\d+]'  # Find the pattern of cell.
        return re.findall(pattern, expression)



utils = Utils