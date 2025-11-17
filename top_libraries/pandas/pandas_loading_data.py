'''
pandas_loading_data.py

'''

import pandas as pd


if False: 
    # create dataframe from scratch, or called creating a dictionary
    data = {'Name':["Tommy","Linda","Justin","Brendon"], 'Age':[31,24,16,22]}
    df=pd.DataFrame(data)
    print(df)


if False:
# load csv file form url
    url = 'https://tinyurl.com/simulated-data'
    dataframe = pd.read_csv(url)
    print(dataframe.head(2))

    # or a csv of titanic passenger data from url
    #url_d = 'https://raw.githubusercontent.com/chrisalbon/sim_data/refs/heads/main/titanic.csv'
    #dataframe_d = pd.read_csv(url_d)
    #pd.DataFrame.to_csv(dataframe_d, 'titanic-data.csv', ',')


if False: 
# load json file
    url_b = 'https://raw.githubusercontent.com/chrisalbon/sim_data/refs/heads/main/data.json'
    dataframe_b = pd.read_json(url_b, orient='columns')
    print(dataframe_b.head(2))


if False: 
    # load excel file
    url_c = 'https://github.com/chrisalbon/sim_data/raw/refs/heads/main/data.xlsx'
    dataframe_c = pd.read_excel(url_c)
    print(dataframe_c.head(2))


if False:
# load csv file from .csv

    dataframe_d = pd.read_csv('titanic-data.csv')
    print(dataframe_d.head(20))
    #print(dataframe_d.shape)
    #print(dataframe_d.describe())
    
    print(dataframe_d[(dataframe_d['Survived'] == 1) & (dataframe_d['Age'] <= 10)].describe())
    print('Max Age: ', dataframe_d['Age'].max())
    print('Num female and age > 50: ', dataframe_d[(dataframe_d['Sex'] == 'female') & (dataframe_d['Age'] >= 50)]['Age'].count())
    print(dataframe_d['Sex'].value_counts())
    print(dataframe_d.groupby('Sex').mean())
    print(dataframe_d.groupby('Survived')['Name'].count()) # groupby Name because groupby needs an operation. we groupby survived then count names
