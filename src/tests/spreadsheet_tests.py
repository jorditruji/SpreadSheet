import unittest
import sys
import os
sys.path.append(os.getcwd()[:os.getcwd().index('src')])
from loguru import logger
from src.spreadsheet import SpreadSheet
from src.cells import ExpressionCell, NumericCell, TextCell
from src.utils import utils


class TestSpreadsheet(unittest.TestCase):

    spreadsheet = SpreadSheet()

    def set_values(self):
        logger.info('Start test setting value types...')
        alias = 'A1'
        value = '10'
        logger.debug('Set {} to cell {}'.format(value, alias))
        self.spreadsheet.set(alias=alias, value=value)

        # Get Numeric cell and check type
        cell, _ = self.spreadsheet.get_cell(alias=alias)
        self.assertIsInstance(cell, NumericCell, 'Type should be numeric.')

        alias = 'A2'
        value = '=A1+1'
        logger.debug('Set \'{}\' to cell {}'.format(value, alias))
        self.spreadsheet.set(alias=alias, value=value)

        # Get Expression cell and check type
        cell, _ = self.spreadsheet.get_cell(alias=alias)
        self.assertIsInstance(cell, ExpressionCell, 'Type should be expression.')

        # Check expression value
        self.assertEqual(cell.value, 11.0, 'Expression result is not correct.')

        alias = 'D1'
        value = 'Hello world'
        logger.debug('Set \'{}\' to cell {}'.format(value, alias))
        self.spreadsheet.set(alias=alias, value=value)

        # Get Text cell and check type
        cell, _ = self.spreadsheet.get_cell(alias=alias)
        self.assertIsInstance(cell, TextCell, 'Type should be text.')

    def copy_cell(self):
        logger.info('Start test copy to single cell...')

        alias = 'C1'
        value = '5'
        logger.debug('Set {} to cell {}'.format(value, alias))
        self.spreadsheet.set(alias=alias, value=value)

        # Copy cell to a sigle cell
        alias_origin = 'A2'
        alias_dest = 'C2'
        self.spreadsheet.copy_cell(alias_origin=alias_origin, range=alias_dest)

        # Get Expression cell and check type
        cell, _ = self.spreadsheet.get_cell(alias=alias_dest)
        self.assertIsInstance(cell, ExpressionCell, 'Type should be expression.')

        # Check if value is correct
        self.assertEqual(cell.value, 6.0, 'Value is not correct')

    def copy_cells(self):
        logger.info('Start test copy to cells range...')

        alias = 'B1'
        value = '7'
        logger.debug('Set {} to cell {}'.format(value, alias))
        self.spreadsheet.set(alias=alias, value=value)

        # Copy cell to a sigle cell
        alias_origin = 'A2'
        alias_dest = 'B2:B6'
        self.spreadsheet.copy_cell(alias_origin=alias_origin, range=alias_dest)

        list_dest = utils.from_range_to_list(range_=alias_dest, letter_list=self.spreadsheet.columns_alias)
        results = [8.0, 9.0, 10.0, 11.0, 12.0]
        for alias_d, result in zip(list_dest, results):
            # Get Expression cell and check type
            cell, _ = self.spreadsheet.get_cell(alias=alias_d)
            self.assertIsInstance(cell, ExpressionCell, 'Type should be expression.')

            # Check if value is correct
            self.assertEqual(cell.value, result, 'Value is not correct')

    def operation(self, alias, value, result, operation_name):
        logger.info('Start testing {} operation...'.format(operation_name))
        self.spreadsheet.set(alias=alias, value=value)

        # Get Expression cell and check type
        cell, _ = self.spreadsheet.get_cell(alias=alias)
        self.assertIsInstance(cell, ExpressionCell, 'Type should be expression.')

        # Check if value is correct
        self.assertEqual(cell.value, result, 'Value is not correct')

    def test(self):
        self.set_values()
        self.copy_cell()
        self.copy_cells()
        self.operation(alias='A3', value='=A1+A2', result=21.0, operation_name='Sum Operand')
        self.operation(alias='A3', value='=SUM(A1:A2)', result=21.0, operation_name='Sum Function')


if __name__ == '__main__':
        unittest.main()


