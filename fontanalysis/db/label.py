from sqlalchemy import Column, Integer, String, ForeignKey

from fontanalysis.db.dbsettings import Base, Session


class Label(Base):
    __tablename__ = 'labels'

    id = Column(Integer, primary_key=True)
    name = Column(String)
