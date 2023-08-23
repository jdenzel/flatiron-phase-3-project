from sqlalchemy import Column, String, Integer, create_engine, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Item(Base):
    __tablename__ = "items"

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    category = Column(String())
    ingredients = Column(String())
    price = Column(Integer())

    def __repr__(self):
        return f"({self.id}, {self.name}, {self.category}, {self.ingredients}, {self.price})"





        