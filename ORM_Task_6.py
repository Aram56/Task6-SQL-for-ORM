import json
import sqlalchemy as sq
from sqlalchemy.orm import sessionmaker


from models_ORM import create_tables, Publisher, Book, Shop, Stock, Sale

DSN = "postgresql://postgres:happy1228@localhost:5432/netology_db"
engine = sq.create_engine(DSN)

conn = engine.connect()



Session = sessionmaker(bind=engine)
session = Session()

create_tables(engine)

with open ('tests_data.json', 'r') as td:
    data = json.load(td)
    
for record in data:
    model = {
        'publisher': Publisher,
        'shop': Shop,
        'book': Book,
        'stock': Stock,
        'sale': Sale
        }[record.get('model')]
    session.add(model(id = record.get('pk'), **record.get('fields')))
    session.commit()

res = input('Введите id:  ')
query_1 = session.query(Publisher).filter(Publisher.id == res)
for c in query_1.all():
    print(f'{c.id}: {c.name}')

# res_2 = input('Введите name:  ')
# query_2 = session.query(Publisher).filter(Publisher.name == res_2)
# for b in query_2.all():
#     print(f'{b.id}: {b.name}')
   
for i in session.query(Shop).join(Stock).join(Book).join(Publisher).filter(Publisher.id == res).all():
    print(f'{i.name}')