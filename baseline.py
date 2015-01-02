import numpy as np 
import pandas as pd

movie_data = pd.io.excel.read_excel( open('movies.xlsx','r') )
print movie_data['title'][0]