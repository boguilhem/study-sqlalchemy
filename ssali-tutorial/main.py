from sqlalchemy import Column, String, Integer, DateTime
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

DB_ACCESS = "gannergui:sp5p^$fw&54DrKV%$piG"
DB_PATH = "@db-learning.cr3z2jnvblyl.us-east-1.rds.amazonaws.com:5432/db_learn"

CONNECTION_STRING = "postgresql://" + DB_ACCESS + DB_PATH

engine = create_engine(
    CONNECTION_STRING,
    echo=True,
)

Base = declarative_base()

Session = sessionmaker()


class User(Base):
    __tablename__ = "users"
    id = Column(Integer(), primary_key=True)
    username = Column(String(25), nullable=False, unique=True)
    email = Column(String(80), nullable=False, unique=True)
    date_created = Column(DateTime(), default=datetime.utcnow)

    def __repr__(self):
        return f"<User username={self.username} email={self.email}>"


# new_user = User(id=1, username="Ronaldo", email="ron@email.com")
# print(new_user)
