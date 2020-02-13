# helper_funcs.py - a few helper functions for data science stuff

import pandas as pd
from sklearn.model_selection import train_test_split
from scipy.stats import chi2_contingency as csc
from IPython.display import display

class DataFrameOperator:
    """Perform pandas.DataFrame operations"""

    def __init__(self, dataframe):
        self.dataframe = dataframe

    def decompose_time(self, feature):
        """Splits a datetime column into year, month
        and day, adds these columns directly to dataframe"""

        if self.dataframe[feature].dtype != '<M8[ns]':
            try:
                self.dataframe[feature] = pd.to_datetime(
                                                 self.dataframe[feature]
                                               )
            except TypeError:
                print("Error: Not a recognized datetime type")

        self.dataframe['year'] = self.dataframe[feature].dt.year
        self.dataframe['month'] = self.dataframe[feature].dt.month
        self.dataframe['day'] = self.dataframe[feature].dt.day

        return self.dataframe

    def auto_split(self):
        """
        Automatically splits into a 64% train, 16% validate and
        20% test set, returns train, val, test
        """
        df = self.dataframe.copy()

        train, test = train_test_split(df, 
                                       test_size=0.2, 
                                       random_state=42)
        train, val = train_test_split(train, 
                                      test_size=0.2, 
                                      random_state=42)

        return train, val, test


def get_chi2(dataframe, f1, f2):
    """Displays a contingency table and prints a chi square report"""

    observed = pd.crosstab(dataframe[f1], dataframe[f2])

    cs, pv, dof, expected = csc(observed)

    display(observed)

    print(f"chi^2: {cs}")
    print(f"p-value: {pv}")
    print(f"dof: {dof}")

if __name__ == "__main__":
    test_df = pd.read_csv('test_data.csv')
    op = DataFrameOperator(test_df)
    train, val, test = op.auto_split()
    
    print(train.shape, val.shape, test.shape, '\n')
    print("DATAFRAME BEFORE DECOMPOSE:\n")
    print(test_df.head(), '\n')
    print("DATAFRAME AFTER DECOMPOSE:\n")
    
    test_df = op.decompose_time('date_recorded')
    
    print(test_df.head())
