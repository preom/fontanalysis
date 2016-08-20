import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlite3 import dbapi2 as sqlite

Base = declarative_base()

engine = create_engine('sqlite:///main.db', echo=False, module=sqlite)

Session = sessionmaker(engine)

mainDbDirPth = os.path.abspath(os.path.dirname(__file__))
mainDepotPth = 'depot'
fntDepotPth = os.path.join(mainDepotPth, 'fontdepot')
imgDepotPth = os.path.join(mainDepotPth, 'imgdepot')

