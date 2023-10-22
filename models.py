from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Numeric
from sqlalchemy.orm import declarative_base, relationship
from datetime import datetime



Base = declarative_base()


class Publisher(Base):
    __tablename__ = "publisher"

    id = Column(Integer, primary_key=True)
    name = Column(String(length=50), unique=True)

    def __str__(self):
        return f"{self.id}: {self.name}"
    def __repr__(self):
        return f"{self.id}: {self.name}"


class Book(Base):
    __tablename__ = "book"

    id = Column(Integer, primary_key=True)
    title = Column(String(length=50), nullable=False)
    id_publisher = Column(Integer, ForeignKey("publisher.id"), nullable=False)

    publisher = relationship(Publisher, backref="book")

    def __str__(self):
        return f"{self.id}: ({self.title}, {self.id_publisher})"


class Shop(Base):
    __tablename__ = "shop"

    id = Column(Integer, primary_key=True)
    name = Column(String(length=30), unique=True)

    def __str__(self):
        return f"{self.id}: {self.name}"



class Stock(Base):
    __tablename__ = "stock"

    id = Column(Integer, primary_key=True)
    id_book = Column(Integer, ForeignKey("book.id"), nullable=False)
    id_shop = Column(Integer, ForeignKey("shop.id"), nullable=False)
    count = Column(Integer, nullable=False)

    book = relationship(Book, backref="stock")
    shop = relationship(Shop, backref="stock")


    def __str__(self):
        return f"{self.id}: ({self.id_book}, {self.id_shop}, {self.count})"


class Sale(Base):
    __tablename__ = "sale"

    id = Column(Integer, primary_key=True)
    price = Column(Numeric(10, 2), nullable=False)
    date_sale = Column(DateTime(timezone=True), default=datetime.utcnow())
    count = Column(Integer, nullable=False)
    id_stock = Column(Integer, ForeignKey("stock.id"), nullable=False)

    stock = relationship(Stock, backref="sale")
    def __str__(self):
        return f"{self.id}: ({self.price}, {self.date_sale}, {self.id_stock}, {self.count})"




def create_table(engine):
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
