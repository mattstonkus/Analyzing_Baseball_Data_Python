import dload
import os.path
from os import path
import pandas as pd


def get_data():
    """
    Function to download lahman data set, unzip and create a folder
    """
    if path.exists('master'):
        print('Folder already exists')
    else:
        dload.save_unzip("https://github.com/chadwickbureau/baseballdatabank/archive/master.zip")


def make_df(data_set: str) -> pd.DataFrame:
    """
    Simple function that saves writting out the file path
    :param data_set: Name of Lahman dataset you want
    :return: A dataframe of the dataset
    """
    assert isinstance(data_set, str)
    df: pd.DataFrame = pd.read_csv(f'master/baseballdatabank-master/core/{data_set}.csv')
    assert isinstance(df, pd.DataFrame)
    return df
