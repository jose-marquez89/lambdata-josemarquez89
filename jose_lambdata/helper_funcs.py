# helper_funcs.py - a few helper functions for data science stuff

import pandas as pd
from sklearn.model_selection import train_test_split

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
    
    
