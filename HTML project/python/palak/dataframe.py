import pandas as pd 


lst = {"Name":["palak", "akhil"],
       "surname": ["shah", "shah"]}

df = pd.DataFrame(lst)
df = df.set_index('Name').reset_index()
# print(df)
lst = ["a","b"]
df4 = pd.DataFrame(lst, columns=['yes'])
# print(df4)
# http://www.datasciencemadesimple.com/indexing-iloc-loc-ix-pandas-python/

d = {
    'Name':['Alisa','Bobby','Cathrine','Alisa','Bobby','Cathrine',
            'Alisa','Bobby','Cathrine','Alisa','Bobby','Cathrine'],
    'Exam':['Semester 1','Semester 1','Semester 1','Semester 1','Semester 1','Semester 1',
            'Semester 2','Semester 2','Semester 2','Semester 2','Semester 2','Semester 2'],
     
    'Subject':['Mathematics','Mathematics','Mathematics','Science','Science','Science',
               'Mathematics','Mathematics','Mathematics','Science','Science','Science'],
   'Score':[62,47,55,74,31,77,85,63,42,67,89,81]}
df3 = pd.DataFrame(d)
# print(df3)
print(type(df3))
print(df3.dtypes)
print("--------------------")
# print(df3.iloc[0:2]) ### by default all columns
# print(df3.iloc[0:2,])
# print("********")
# print(df3.iloc[5])  ### act for index
# print(df3.iloc[:5])  ## range

# print(df3.iloc[:,:2])

# print(df3.iloc[1])
# print("_____________")
# print(df3.loc[1])

