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