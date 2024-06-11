from settings import Base,SQLALCHEMY_DB_URI
from sqlalchemy import Column,BIGINT,VARCHAR
class User(Base):
    __tablename__ = "user"
    id = Column(BIGINT,autoincrement = True,primary_key = True)
    uname = Column(VARCHAR(255) )
    pwd = Column(VARCHAR(64))