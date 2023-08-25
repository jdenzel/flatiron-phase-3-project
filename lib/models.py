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
    
class Customer(Base):
    __tablename__ = "customers"

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    phone_number = Column(String())
    orders = relationship("Order", backref="customers")

    def __repr__(self):
        return f"({self.id}, {self.name}, {self.phone_number} {self.orders})"

class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer(), primary_key=True)
    items = Column(String())
    total_price = Column(Float())
    customer_id = Column(Integer(), ForeignKey("customers.id"))

    def __repr__(self):
        return f"({self.id}, {self.item},  {self.total_price}, {self.customer_id})"
    


    
    



    




        