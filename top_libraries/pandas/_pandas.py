'''
Pandas is a library for data manipulation and analysis. It offers data structres and operations for 
manipulating numberical tables and time series. 
'''

import pandas as pd

if False: 
    # create dataframe from scratch, or called creating a dictionary
    data = {'Name':["Tommy","Linda","Justin","Brendon"], 'Age':[31,24,16,22]}
    df=pd.DataFrame(data)
    print(df)



df = pd.read_csv("http://rcs.bu.edu/examples/python/data_analysis/Salaries.csv")
print(df)
#pd.read_excel('myfile.xlsx',sheet_name='Sheet1', index_col=None, na_values=['NA'])
#pd.read_stata('myfile.dta')
#pd.read_sas('myfile.sas7bdat')
#pd.read_hdf('myfile.h5','df')
