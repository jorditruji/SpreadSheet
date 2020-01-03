from .expression_cell import ExpressionCell
from .numeric_cell import NumericCell
from .text_cell import TextCell


class CellFactory:

    @staticmethod
    def create_cell(type, params):
        return globals()[type](params)
