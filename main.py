from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from models import Publisher, Book, Shop, Stock, Sale, create_table
from json import load
import os
from dotenv import load_dotenv

def write_data(data_name):
    with open(data_name, encoding='utf-8') as file:
        return load(file)

def write_table(data):
    models_dictionary = {
        Publisher.__tablename__: Publisher,
        Book.__tablename__: Book,
        Shop.__tablename__: Shop,
        Stock.__tablename__: Stock,
        Sale.__tablename__: Sale
    }
    with Session(engine) as session:
        for row in data:
            model = models_dictionary.get(row.get('model'))
            if model:
                session.add(model(**row.get('fields')))
                session.commit()

def make_query(author):
    with Session(engine) as session:
        if author.isdigit():
            q = session.query(Publisher, Book.title, Shop.name, Sale.price, Sale.date_sale) \
                .join(Book) \
                .join(Stock).join(Shop).join(Sale) \
                .filter((Publisher.id == author)).all()
            return q
        else:
            q = session.query(Publisher, Book.title, Shop.name, Sale.price, Sale.date_sale) \
                .join(Book) \
                .join(Stock).join(Shop).join(Sale) \
                .filter((Publisher.name == author)).all()
            return q

def print_data(data):
    size_title_book, size_name_shop = [len(x[1]) for x in data], [len(x[2]) for x in data]
    for publisher, title, shop_name, price, date_sale in data:
        print(f"{title.ljust(max(size_title_book))} | {shop_name.ljust(max(size_name_shop))} | {price} | {date_sale}")

def get_book():
    author = input('Введите id издателя или название:')
    q = make_query(author)
    if q:
        print_data(q)
    else:
        print('Данные не найдены')



if __name__ == '__main__':
    load_dotenv()
    engine = create_engine(f"{os.getenv('NAME_DRIVER')}://"
                           f"{os.getenv('USER')}:"
                           f"{os.getenv('PASSWORD')}@"
                           f"localhost:{os.getenv('LOCAL_HOST')}/"
                           f"{os.getenv('DB')}")
    create_table(engine)

    write_table(write_data('tests_data.json'))
    get_book()

