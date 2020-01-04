import sys
import os
sys.path.append(os.getcwd()[:os.getcwd().index('src')])

from src.spreadsheet import SpreadSheet

spreadsheet = SpreadSheet()

# Initialize test
list_sets = [
    {"alias": "A1", "value": '10'},
    {"alias": "A2", "value": '10'},
    {"alias": "B1", "value": '5'},
    {"alias": "B2", "value": '5'},
    {"alias": "B4", "value": '20'},
    {"alias": "A4", "value": '15'},
    {"alias": "A3", "value": "=average(A1:A2,A4)"}
]

for set in list_sets:
    spreadsheet.set(alias=set['alias'], value=set['value'])

spreadsheet.copy_cell(alias_origin='A3', range='B3')
cell, _ = spreadsheet.get_cell(alias='B3')
if cell.value == 10.0:
    cell.printify()
else:
    print('ERROR')