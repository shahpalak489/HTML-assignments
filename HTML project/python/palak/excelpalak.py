import pandas as pd

df = pd.read_excel(open('frm/movies.xls', 'rb'), sheet_name='2010s')
print(df)
