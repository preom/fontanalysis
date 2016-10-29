import pprint 

from fontanalysis.db.dbsettings import engine, Base
#import font
import fontlabel

pprint.pprint("Tables: ")
pprint.pprint(Base.metadata.tables.keys())
Base.metadata.create_all(engine)
