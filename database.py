from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

"""dialect+driver://username:password@host:port/database"""
LOCAL_DB_URL = "mysql://root:Mysql07052022@localhost:3306/localdbtest"
REMOTE_DB_URL = "mysql://...{Define your remote database URL here...}"

engine = create_engine(LOCAL_DB_URL, pool_pre_ping=True)  # connect with the sql server

"""scoped_session in short provides thread safety: several threads can share the same connection."""
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))  # session, like conversation instance with the db

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
    """Create SQL tables from classes that extend Base!"""
    import models
    Base.metadata.create_all(bind=engine)


def drop_db():
    import models
    Base.metadata.drop_all(bind=engine)
