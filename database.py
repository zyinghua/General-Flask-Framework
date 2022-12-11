from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

"""dialect+driver://username:password@host:port/database"""
LOCAL_DB_URL = "mysql://... {Define your local database URL here...}"
REMOTE_DB_URL = "mysql://...{Define your remote database URL here...}"

engine = create_engine(LOCAL_DB_URL, pool_pre_ping=True)

"""scoped_session in short provides thread safety: several threads can share the same connection."""
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))

""" 
declarative_base() is a factory function that constructs a base class 
for declarative class definitions. Or, it helps configure ORM (Object Relational Mapping). 
Otherwise you have to do the ORM manually.
"""
Base = declarative_base()
Base.query = db_session.query_property()


def init_db():
    # import all modules here that might define models so that
    # they will be registered properly on the metadata. Otherwise,
    # you will have to import them first before calling init_db()
    Base.metadata.create_all(bind=engine)


def drop_db():
    Base.metadata.drop_all(bind=engine)