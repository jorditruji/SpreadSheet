from .expression_cell import ExpressionCell
from .numeric_cell import NumericCell
from .text_cell import TextCell


class CellFactory:

    @staticmethod
    def create_cell(typ, params):
        return globals()[typ](params)
