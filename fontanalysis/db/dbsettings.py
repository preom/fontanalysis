from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlite3 import dbapi2 as sqlite

Base = declarative_base()

engine = create_engine('sqlite:///main.db', echo=True, module=sqlite)

Session = sessionmaker(engine)

