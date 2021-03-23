import dload
import os.path
import os
import pandas as pd


def get_data():
    """
    Function to download lahman data set, unzip and create a folder
    """
    if os.path.exists('master'):
        print('Folder already exists')
    else:
        dload.save_unzip("https://github.com/chadwickbureau/baseballdatabank/archive/master.zip", delete_after=True)


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

def get_retro_data():
    retro_path = './retro'
    os.mkdir(retro_path)
    for year in range(1871,2020):
        dload.save_unzip(f'https://www.retrosheet.org/gamelogs/gl{year}.zip', extract_path=retro_path , delete_after=True)
