from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
Base = declarative_base()
SQLALCHEMY_DB_URI = "sqlite///./db2.db"
engine = create_engine(SQLALCHEMY_DB_URI)
db_session =  sessionmaker(engine)