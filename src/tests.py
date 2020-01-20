import unittest
from src.tests import TestSpreadsheet
import sys
import os
sys.path.append(os.getcwd()[:os.getcwd().index('src')])

if __name__ == '__main__':
    unittest.main()