from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class Publisher(Base):
    __tablename__ = "publisher"

    publisher_id = Column(Integer, primary_key=True)
    name = Column(String(length=50), unique=True)

    def __str__(self):
        return f"{self.publisher_id}: {self.name}"

class Book(Base):
    __tablename__ = "book"

    book_id = Column(Integer, primary_key=True)
    title = Column(String(length=50), nullable=False)
    publisher_id = Column(Integer, ForeignKey=True, nullable=False)

    publisher = relationship(Publisher, backref="book")

    def __str__(self):
        return f"{self.book_id}: ({self.title}, {self.publisher_id})"

class Shop(Base):
    __tablename__ = "shop"

    shop_id = Column(Integer, primary_key=True)
    name = Column(String(length=(30)), unique=True)

    def __str__(self):
        return f"{self.shop_id}: {self.name}"

class Sale(Base):
    pass