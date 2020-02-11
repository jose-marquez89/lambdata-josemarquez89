# helper_funcs.py - a few helper functions for data science stuff

import pandas as pd
from sklearn.model_selection import train_test_split
from scipy.stats import chi2_contingency as csc
from IPython.display import display 

def auto_split(dataframe):
    """Automatically splits into a 64% train, 16% validate and
    20% test set, returns train, val, test
    """
    df = dataframe.copy()
    
    train, test = train_test_split(df, test_size=0.2, random_state=42)
    train, val = train_test_split(train, test_size=0.2, random_state=42)
    
    return train, val, test
    
def decompose_time(dataframe, date_feature):
    """Splits a datetime column into year, month
    and day, adds these columns directly to dataframe"""
    
    if dataframe[date_feature].dtype != '<M8[ns]':
        try:
            dataframe[date_feature] = pd.to_datetime(dataframe[date_feature])
        except TypeError:
            print("Error: Not a recognized datetime type")
    
    dataframe['year'] = dataframe[date_feature].dt.year
    dataframe['month'] = dataframe[date_feature].dt.month
    dataframe['day'] = dataframe[date_feature].dt.day
    
    return dataframe
    
def get_chi2(dataframe, f1, f2):
    """Displays a contingency table and prints a chi square report"""
    
    observed = pd.crosstab(dataframe[f1], dataframe[f2])
    
    cs, pv, dof, expected = csc(observed)
    
    display(observed)
    
    print(f"chi^2: {cs}")
    print(f"p-value: {pv}")
    print(f"dof: {dof}")
    
    return None
    
    
    
    
