import unittest
import sys
import os
sys.path.append(os.getcwd()[:os.getcwd().index('src')])
from loguru import logger
from src.spreadsheet import SpreadSheet
from src.cells import ExpressionCell as expression, NumericCell as numeric, TextCell as text
from src.utils import utils


class TestSpreadsheet(unittest.TestCase):

    spreadsheet = SpreadSheet()

    def set_value(self, alias, value, result):
        logger.info('Test set value...')
        logger.debug('TEST: Set {} to cell {}'.format(value, alias))
        self.spreadsheet.set(alias=alias, value=value)

        # Get Numeric cell and check type
        cell, _ = self.spreadsheet.get_cell(alias=alias)
        self.assertIsInstance(cell, globals()[cell.type], 'Type is {}.'.format(cell.type))

        # Check expression value
        self.assertEqual(cell.value, result, 'Result is not correct.')

        logger.success('ok!')

    def copy_cell(self, alias_origin, alias_dest, result):
        logger.info('Test copy {} to {}...'.format(alias_origin, alias_dest))

        # Copy cell to a sigle cell
        self.spreadsheet.copy_cell(alias_origin=alias_origin, range=alias_dest)

        # Get Expression cell and check type
        cell, _ = self.spreadsheet.get_cell(alias=alias_dest)
        self.assertIsInstance(cell, globals()[cell.type], 'Type should be expression.')

        # Check if value is correct
        self.assertEqual(cell.value, result, 'Value is not correct')

        logger.success('ok!')

    def copy_cells(self, alias_origin, alias_dest, results):
        logger.info('Test copy to cells range...')

        # Copy cell to a sigle cell
        self.spreadsheet.copy_cell(alias_origin=alias_origin, range=alias_dest)

        list_dest = utils.from_range_to_list(range_=alias_dest, letter_list=self.spreadsheet.columns_alias)

        for alias_d, result in zip(list_dest, results):
            # Get Expression cell and check type
            cell, _ = self.spreadsheet.get_cell(alias=alias_d)
            self.assertIsInstance(cell, expression, 'Type should be expression.')

            # Check if value is correct
            self.assertEqual(cell.value, result, 'Value is not correct')

        logger.success('ok!')

    def save_load(self, name):
        logger.info('Test saving spreadsheet...')
        self.spreadsheet.save(name=name, path_='../resources/')
        logger.debug('Loading saved spreadsheet')
        loaded_spreadsheet = self.spreadsheet.load(name=name, path_='../resources/')

        self.assertEqual(self.spreadsheet, loaded_spreadsheet, 'Spreadsheets are not equal.')
        logger.success('ok!')

    def test(self):
        try:
            # Test set cell of every type
            self.set_value(alias='A1', value='10', result=10.0)
            self.set_value(alias='A2', value='=A1+1', result=11.0)
            self.set_value(alias='D1', value='Hello World!', result='Hello World!')

            # TODO: parsing decimals not supported !!!!!
            #self.set_value(alias='C1', value='7.5', result=7.5)
            self.set_value(alias='C1', value='7', result=7.0)

            # Test copy cells
            self.copy_cell(alias_origin='A2', alias_dest='C2', result=7.0+1)

            self.set_value(alias='B1', value='6', result=6.0)
            results = [7.0, 8.0, 9.0, 10.0, 11.0]
            self.copy_cells(alias_origin='A2', alias_dest='B2:B6', results=results)

            # Test operations and functions
            self.set_value(alias='A3', value='=A1+A2', result=21.0)
            self.set_value(alias='A4', value='=A1*A2', result=110.0)
            self.set_value(alias='A5', value='=A2/A1', result=1.1)
            self.set_value(alias='A6', value='=mean(A1:A2)', result=10.5)
            self.set_value(alias='A7', value='=SUM(A1:A2)', result=21.0)
            self.set_value(alias='A8', value='=sum($A$1:A2, SUM($B$1:$B$2))', result=34.0)

            #self.copy_cell(alias_origin='A8', alias_dest='B8', result=47.0)

            self.save_load('test')

        except Exception as e:
            logger.error(e.custom_message)
            raise e


if __name__ == '__main__':
        unittest.main()


