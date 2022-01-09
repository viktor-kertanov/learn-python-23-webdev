from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session, declarative_base

engine = create_engine("postgresql://zvhjcykr:Kyiq4Rq2pPM314A4kk1TFtmRBxeMdyZY@abul.db.elephantsql.com/zvhjcykr")
db_session = scoped_session(sessionmaker(bind=engine))

Base = declarative_base()
Base.query = db_session.query_property
    
