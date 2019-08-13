import sqlalchemy
from sqlalchemy.orm import sessionmaker
import pandas as pd 
import flask

engine = sqlalchemy.create_engine('mssql+pyodbc://LAPTOP-QDH3PMIF/master?driver=SQL+Server+Native+Client+11.0')
connection = engine.connect()
metadata = sqlalchemy.MetaData()
sqlQ = sqlalchemy.Table('userinfo', metadata, autoload=True, autoload_with=engine)
# print(sqlQ.columns.keys())

qAns = sqlalchemy.select([sqlQ])
ResultProxy = connection.execute(qAns)
ResultSet = ResultProxy.fetchall()
# print(ResultSet)
df = pd.DataFrame(ResultSet, columns=['firstname', 'lastname', 'ID'])
jsonData = df.to_json(orient="records")
print(jsonData)