class AliasNotFound(Exception):
    """Raised when the input alias value is not found"""
    def __init__(self, row=None, col=None):
        self.custom_message = ''
        if col is not None:
            self.custom_message = 'Column {} does not exist'.format(col)
        if row is not None:
            self.custom_message = 'Row {} does not exist'.format(row)


class CellNotFound(Exception):
    """Raised when the cell does not exist"""
    def __init__(self, alias):
        self.custom_message = 'There is no content in cell: {}'.format(alias)


class PathNotFound(Exception):
    """Raised when a path does not exist"""
    def __init__(self, path):
        self.custom_message = '{} does not exist'.format(path)

class CopyAlias(Exception):
    """Raised when caopying a cell, the calculated reference aliases in expression cannot be found"""
    def __init__(self, alias_origin, alias_dest):
        self.custom_message = 'Alias {} cannot be converted to alias {}'.format(alias_origin, alias_dest)

class EmptySpreadsheet(Exception):
    """Raised when an empty spreadsheet wants to be saved"""
    def __init__(self):
        self.custom_message = 'The is no content in the spreadsheet'

class FailedToEvaluateExpression(Exception):
    """Raised when an expression cannot be evaluated"""
    def __init__(self, alias):
        self.custom_message = 'Failed to evaluate expression in {}'.format(alias)

class EmptyInvolvedCells(Exception):
    """Raised when Involved cells have no value"""
    def __init__(self, alias):
        self.custom_message = 'Cell {} is empty, Expression cannot be evaluated'.format(alias)


