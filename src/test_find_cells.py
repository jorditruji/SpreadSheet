import sys
import os
sys.path.append(os.getcwd()[:os.getcwd().index('src')])

from src.expression_parser import ExpressionParser

expression = 'average(B1:B3;$B$1)'

expression_parser = ExpressionParser()
a = expression_parser.find_cells(expression=expression)
print(a)

