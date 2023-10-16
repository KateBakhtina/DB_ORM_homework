# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker
# import models
#
#
# engine = create_engine(f"{input('Драйвер подключения: ')}://"
#                            f"{input('Пользователь: ')}:"
#                            f"{input('Пароль: ')}@"
#                            f"localhost:{input('порт: ')}/"
#                            f"{input('База данных: ')}")
#
# models.create_table(engine)
#
# Session = sessionmaker(bind=engine)
# session = Session()


from dotenv import dotenv_values
config = dotenv_values()        
print(config.get('NAME_DRIVER'))





