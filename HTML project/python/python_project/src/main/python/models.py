from sqlalchemy import Column, Date, Integer, Boolean, String
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class cUserInfo(Base):
	__tablename__   = "userinfo"
	__table_args__ = {'schmema' : 'dbo'}
	ID = Column(Integer, primery_key = True)
	firstname = Column(String(64), primery_key = True)
	lastname = Column(String(64))