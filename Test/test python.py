from pydoc import describe
import pandas as pd 
import matplotlib as plt
import numpy as np
do = pd.read_excel ('titanic3 (3).xls')   #read the csv file (put 'r' before the path string to address any special characters in the path, such as '\'). Don't forget to put the file name at the end of the path + ".csv"
print(do)
do.shape
do.head()
do.describe
