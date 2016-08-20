from fontanalysis.db.dbsettings import Base
from sqlalchemy import Column, Integer, String, ForeignKey

class Font(Base):
    __tablename__ = 'fonts'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    ext = Column(String)
    src = Column(String)

    def __repr__(self):
        return "id: {}, name: {}".format(self.id, self.name)

class FontImage(Base):
    __tablename__ = 'fontimage'

    id = Column(Integer, primary_key=True)    
    fontname = Column(Integer, ForeignKey("fonts.id"), nullable=False)    
    character = Column(String(1))    

