from sqlalchemy import String , Integer , Column , Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = "user"
    username = Column(String(500), primary_key=True)
    password = Column(String(500))


class Admin(Base):
    __tablename__ = "admin"
    username = Column(String(500), primary_key=True)
    password = Column(String(500))

class Guild(Base):
    __tablename__ = "guild"
    id = Column(Integer , primary_key=True)
    name = Column(String(500))
    member_count = Column(Integer)
    ban = Column(Boolean , default=False)
    context = Column(String(1000))
    username = Column(String(500))

class Verify(Base):
    __tablename__ = "verify"
    username = Column(String(500), primary_key=True)
    otp = Column(String(10))

def create(engine):
    Base.metadata.create_all(engine)

