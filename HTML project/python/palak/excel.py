import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile

# df = pd.read_excel('frm/practice.xlsx', header = 0)

# print("Column headings:")
# print(df)


# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_excel.html


import xlwt 
  
workbook = xlwt.Workbook()  
  
sheet = workbook.add_sheet("Sheet Name") 
  
# Specifying style 
# style = xlwt.easyxf('font: bold 1') 
  
  
# Specifying column 
sheet.write(0, 0, 'SAMPLE') 
# sheet.write(0, 0, 'SAMPLE', style) 
workbook.save("frm/sample.xls") 
