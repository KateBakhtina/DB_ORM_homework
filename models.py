from sqlalchemy import Column, Integer, String, ForeignKey, Float, DateTime
from sqlalchemy.orm import declarative_base, relationship
from datetime import datetime


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
    publisher_id = Column(Integer, ForeignKey("publisher.publisher_id"), nullable=False)

    publisher = relationship(Publisher, backref="book")

    def __str__(self):
        return f"{self.book_id}: ({self.title}, {self.publisher_id})"


class Shop(Base):
    __tablename__ = "shop"

    shop_id = Column(Integer, primary_key=True)
    name = Column(String(length=30), unique=True)

    def __str__(self):
        return f"{self.shop_id}: {self.name}"


class Stock(Base):
    __tablename__ = "stock"

    stock_id = Column(Integer, primary_key=True)
    book_id = Column(Integer, ForeignKey("book.book_id"), nullable=False)
    shop_id = Column(Integer, ForeignKey("shop.shop_id"), nullable=False)
    amount = Column(Integer, nullable=False)

    book = relationship(Book, backref="stock")
    shop = relationship(Shop, backref="stock")

    def __str__(self):
        return f"{self.stock_id}: ({self.book_id}, {self.shop_id}, {self.amount})"


class Sale(Base):
    __tablename__ = "sale"

    sale_id = Column(Integer, primary_key=True)
    price = Column(Float(2), nullable=False)
    date_sale = Column(DateTime(timezone=True), default=datetime.utcnow())
    stock_id = Column(Integer, ForeignKey("stock.stock_id"), nullable=False)
    amount = Column(Integer, nullable=False)

    def __str__(self):
        return f"{self.sale_id}: ({self.price}, {self.date_sale}, {self.stock_id}, {self.amount})"

    stock = relationship(Stock, backref="sale")


def create_table(engine):
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
