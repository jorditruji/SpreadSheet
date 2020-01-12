import sys
import os
sys.path.append(os.getcwd()[:os.getcwd().index('src')])

from src.utils import utils

expression = 'average(B1:B3;$B$1)'

a = utils.find_cells(expression=expression)
print(a)

