import dload
import os.path
from os import path

if path.exists('master'):
    print('Folder already exists')
else:
    dload.save_unzip("https://github.com/chadwickbureau/baseballdatabank/archive/master.zip")