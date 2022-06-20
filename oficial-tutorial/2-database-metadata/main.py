from sqlalchemy import create_engine, MetaData, ForeignKey

engine = create_engine("sqlite+pysqlite:///:memory:", echo=True, future=True)

metadata_obj = MetaData()

### -------- USING CORE -------- ###
# from sqlalchemy import Table, Column, Integer, String

# user_table = Table(
#     "user_account",
#     metadata_obj,
#     Column("id", Integer, primary_key=True),
#     Column("name", String(30)),
#     Column("fullname", String),
# )

# address_table = Table(
#     "address",
#     metadata_obj,
#     Column("id", Integer, primary_key=True),
#     Column("user_id", ForeignKey("user_account.id"), nullable=False),
#     Column("email_address", String, nullable=False),
# )

# metadata_obj.create_all(engine)


### -------- USING ORM -------- ###

## OLD WAY OF CREATING REGISTRY (registry -> mapper -> Base)
# from sqlalchemy.orm import registry

# mapper_registry = registry()
# Base = mapper_registry.generate_base()

## NEW WAY OF CREATING REGISTRY (declarative_base)
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class User(Base):
    __tablename__ = "user_account"
    id = Column(Integer, primary_key=True)
    name = Column(String(30))
    fullname = Column(String)

    addresses = relationship("Address", back_populates="user")

    def __repr__(self):
        return f"User(id={self.id!r}, name={self.name!r}, fullname={self.fullname!r})"


class Address(Base):
    __tablename__ = "address"
    id = Column(Integer, primary_key=True)
    email_address = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey("user_account.id"))

    user = relationship("User", back_populates="addresses")

    def __repr__(self):
        return f"Address(id={self.id!r}, email_address={self.email_address!r})"
