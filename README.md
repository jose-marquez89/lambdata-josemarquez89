# Jose's Lambdata Package
A set of tools for pandas dataframe operations

## Installation
To install `jose_lambdata` use `pip`:
```
pip install -i https://test.pypi.org/simple/ lambdata-josemarquez89
```

## Usage
As of this release, there are 2 main tools in the package. The 
`DataFrameOperator` class contains a `.decompose_time()` method that allows
decomposition of full date columns into separate year, month and day features, 
while `.auto_split()` automatically splits into a train, validate and test set.
The second tool in the package is the `get_chi2()` function, which returns a
contingency table along with a chi squared report.

You can instantiate the `DataFrameOperator` and use its methods as shown below:
```python
import pandas as pd
from jose_lambdata.dftools import DataFrameOperator

df = pd.read_csv('some_url.csv')

df_operator = DataFrameOperator(df)

train, val, test = df_operator.auto_split()

df_operator.decompose_time('some_date_feature')
```

To use the `get_chi2()` function:
```python
get_chi2(df, 'first_feature', 'second_feature')
```
This will return a contingency table with IPython and uses sklearn to get 
chi squared, the p value and degrees of freedom.




