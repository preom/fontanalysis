from base import Base, Session, engine

Base.metadata.create_all(engine)


testFont = Font(name='testing', fname='testing.tff')
session = Session()
session.add(testFont)
session.commit()








