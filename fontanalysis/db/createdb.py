from fontanalysis.db.dbsettings import engine, Base
import font

Base.metadata.create_all(engine)
