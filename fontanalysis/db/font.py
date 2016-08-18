from fontanalysis.db.dbsettings import Base
from sqlalchemy import Column, Integer, String

class Font(Base):
    __tablename__ = 'fonts'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    fname = Column(String)

    def __repr__(self):
        return "id: {}, name: {}, fname: {}".format(self.id, self.name, self.fname)
