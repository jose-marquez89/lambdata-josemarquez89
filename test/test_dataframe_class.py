import unittest

import pandas as pd
from jose_lambdata.dftools import DataFrameOperator

class TestDFO(unittest.TestCase):
	
	def test_decompose_time(self):
		df = pd.read_csv('test_data.csv')
		op = DataFrameOperator(df)
		df = op.decompose_time('date_recorded')
		new_cols = ['year', 'month', 'day']
		
		self.assertTrue(all(x in df.columns for x in new_cols))
	
	def test_auto_split(self):
		df = pd.read_csv('test_data.csv')
		op = DataFrameOperator(df)
		train, val, test = op.auto_split()
		
		self.assertTrue((train.shape[0] > val.shape[0]) & 
						(train.shape[0] > test.shape[0]) & 
						(train.shape[0] < df.shape[0]))
						
if __name__ == "__main__":
	unittest.main()
						
		
