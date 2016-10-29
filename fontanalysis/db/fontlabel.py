from sqlalchemy import Column, Integer, String, ForeignKey

from font import Font
from label import Label
from fontanalysis.db.dbsettings import Base


class FontLabel(Base):
    __tablename__ = 'fontslabel'

    id = Column(Integer, primary_key=True)
    font_id = Column(Integer, ForeignKey(Font.__table__.c.id))
    label_id = Column(Integer, ForeignKey(Label.__table__.c.id))

