from sqlalchemy import Column, String, Integer, Float, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Item(Base):
    __tablename__ = "items"

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    category = Column(String())
    ingredients = Column(String())
    spice_level = Column(Integer())
    price = Column(Float())

    def __repr__(self):
        return f"({self.id}, {self.name}, {self.category}, {self.ingredients}, {self.price})"

class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer(), primary_key=True)
    items_ordered = Column(String(), ForeignKey("items.id"))
    total_price = Float(Integer())

    def __repr__(self):
        return f"({self.id}, {self.item_id}, {self.quantity}, {self.total_price})"

class Customer(Base):
    __tablename__ = "customers"

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    order_id = Column(Integer(), ForeignKey("orders.id"))

    def __repr__(self):
        return f"({self.id}, {self.name}, {self.order_id})"
    
class Restaurant(Base):
    __tablename__ = "restaurants"

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    customers = Column(Integer(),  ForeignKey("customers.id"), unique=True)


    
    



    




        