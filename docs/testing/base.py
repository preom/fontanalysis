from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlite3 import dbapi2 as sqlite

Base = declarative_base()

engine = create_engine('sqlite:///main.db', module=sqlite, echo=True)

Session = sessionmaker()
Session.configure(bind=engine)


class Font(Base):
    __tablename__ = 'fonts'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    fname = Column(String)

    def __repr__(self):
        return "id: {}, name: {}, fname: {}".format(id, name, fname)
   

