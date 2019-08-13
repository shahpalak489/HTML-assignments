### using pyodbc
# import pyodbc 
# conn = pyodbc.connect('Driver={SQL Server};'
#                       'Server="LAPTOP-QDH3PMIF;'
#                       'Database=master;'
#                       'Trusted_Connection=yes;')

# cursor = conn.cursor()
# cursor.execute('SELECT * FROM dbo.userinfo')

# for row in cursor:
#     print(row)

    # Native Client 11.0

### using sqlalchemy

import sqlalchemy
# from models import *
from sqlalchemy.orm import sessionmaker
import pandas as pd 
engine = sqlalchemy.create_engine('mssql+pyodbc://LAPTOP-QDH3PMIF/master?driver=SQL+Server+Native+Client+11.0')
# Session = sessionmaker(bind=engine)
# session = Session()
connection = engine.connect()
metadata = sqlalchemy.MetaData()
sqlQ = sqlalchemy.Table('userinfo', metadata, autoload=True, autoload_with=engine)
# print(sqlQ.columns.keys())

qAns = sqlalchemy.select([sqlQ])  ### select q
# print(qAns)

ResultProxy = connection.execute(qAns)
ResultSet = ResultProxy.fetchall()
# print(ResultSet)
df = pd.DataFrame(ResultSet, columns=['firstname', 'lastname', 'ID'])
print(df)