from locale import D_FMT
import pandas as pd
import numpy as np

# data = pd.read_csv('Pandas/cvs/nba.csv',index_col= "Name")
# first = data.loc["Avery Bradley"]     #selecting row by Name(index_col)
# second = data.loc["R.J. Hunter"]
# row_5 = data.iloc[5]      #selecting single row by index number
# print(first, "\n\n\n", second)
# print(first["College"])

#FUNCTIONS
# print(data.head(5))                           #print first n rows
# print(data.at['Kelly Olynyk','Age'])          #selecting cell by row and colounm
# print(data.iat[7,3])                          #selecting cell by int(row) and int(colounm)
# print(data.tail(5))                           #print last n rows
# print(data.get(["Age", "College"]))           #extract single or multiple colounm
# new = data["Team"].isin(['Brooklyn Nets'])    #Create new dataset with any contained value
# print(data[new])




# dict = {'Date': ['2022-5-1','2022-5-5','2022-5-10'], 'Name': ["smitesh","Kunj","Mohit"], 'Age':[21,np.nan,np.nan], 'Field': ["IT",np.nan,np.nan]}
# d_frame = pd.DataFrame(dict)

# d_frame.dropna(0,thresh=3, inplace=True)
# print(d_frame)
# dte = pd.date_range('2022-5-1','2022-5-10')
# dte_idx = pd.DatetimeIndex(dte)
# d_frame = d_frame.reindex(dte_idx)
# print(d_frame)

# for i,j in d_frame.iterrows():
#     print(i,j)

# colunms = list(d_frame)
# for i in colunms:
#     print(d_frame[i][0])

# temp = pd.notnull(d_frame['Age'])
# print(temp)

# print(d_frame.isnull())
# print(d_frame.notnull())
# print(d_frame.fillna('fillna'))
# print(d_frame.replace(np.nan,'replaced'))




dict = {'a': [1,8,3],'b': [4,5,6],'c': [7,8,9]}
d_frame = pd.DataFrame(dict)
print(d_frame.query('a == c'))


print(pd.Series(dict), Index=[22,33,55])

