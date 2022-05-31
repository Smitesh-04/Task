from audioop import reverse
from matplotlib.pyplot import margins
import pandas as pd
import numpy as np

# data = pd.read_csv('Pandas/nba.csv',index_col='Name')
# d_frame = pd.DataFrame(data)

#SORTING
# d_frame.sort_values(by=['Name'], inplace=True)
# print(d_frame)


#GROUP BY
# print(d_frame.groupby(by='College').Age.mean())       #group by specifies colounm
# print(d_frame['College'].value_counts())      #Count occurance of unique values

#BOOLEAN INDEXING
# dict = {'a': [1,8,3],'b': [4,5,6],'c': [7,8,9]}
# d_frame = pd.DataFrame(dict, index=[True,False,True])
# print(d_frame.loc[])

#BLOOLEAN MASKING
# dict = {'a': [1,8,3],'b': [4,5,6],'c': [7,8,9]}
# d_frame = pd.DataFrame(dict, index=[0,1,2])
# print(d_frame[[True,False,True]])

# dict = {'a': [1,8,3],'b': [4,5,np.nan],'c': [7,8,9]}
# d_frame = pd.DataFrame(dict, index = ['s','m','i'])
# print(d_frame['a']==8)
# print(d_frame.index)
# print(d_frame.describe())
# print(d_frame.memory_usage(index = True ,deep=True))
# print(d_frame.astype('float32').dtypes)



#MERGING --> default = inner
# d1 = {'Country': ['India','USA', 'Africa', 'Germany', 'Romania', 'Ukrain'], 'Temperature': [44,35.5,49.99,20,35,45]}
# d2 = {'Country': ['India','USA', 'Africa', 'Germany', 'Iceland'], 'Humidity': [22,33,25,10,15]}
# d2 = {'Country': ['India','USA', 'Africa', 'Germany', 'Romania', 'Ukrain'], 'Temperature': [44,35.5,49.99,20,35,45]}
# df1 = pd.DataFrame(d1)
# df2 = pd.DataFrame(d2)
# df3 = pd.merge(df1,df2,on='Country', how='left', indicator=True)
# df3 = pd.merge(df1, df2, on='Country', suffixes=('-d1', '-d2'))
# print(df3)
 

#PIVOT_TABLE --> groups similar data, by default = 'mean'
# d1 = {'date':  ['5/1/2017','5/1/2017','5/2/2017','5/2/2017','5/1/2017','5/1/2017', '5/2/2017', '5/2/2017'], 'Country': ['India','India', 'India', 'India', 'Germany', 'Germany', 'Germany', 'Germany'], 'Temperature': [44,35.5,49.99,20,35,45,50,30], 'Humidity': [44,35.5,49.99,20,35,45,45,33]}
# d_frame = pd.DataFrame(d1)
# d_frame['date'] = pd.to_datetime(d_frame['date'])
# print(d_frame.pivot_table(index='Country', columns='date', aggfunc='sum', margins=True))
# print(d_frame.pivot_table(index=pd.Grouper(freq='D', key='date'), columns='Country'))       #gouper



#MELT
data = {'Day': ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'], 'City': ['Mumbai','Chicago', 'Munich', 'New York', 'Istanbul', 'Madrid'], 'Temperature': [1,2,3,4,5,6]}
d_frame = pd.DataFrame(data)
print(d_frame.melt(data, id_vars=["Days"]))