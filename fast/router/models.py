from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.engine import URL
from sqlalchemy.orm import declarative_base, sessionmaker


url = URL.create(
    drivername="postgresql",
    username="postgres",
    password="admin",
    host="localhost",
    database="InBytes",
    port=5432
)

engine = create_engine(url)
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

class Login2(Base):
    __tablename__ = "login"

    userid = Column(Integer, primary_key=True)
    password = Column(String)


Base.metadata.create_all(engine)


class UserProfile(BaseModel):
    userid: int
    userName: str
    userBio: str

class Login(BaseModel):
    userid: int
    password: str