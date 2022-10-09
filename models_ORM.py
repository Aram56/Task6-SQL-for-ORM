import sqlalchemy as sq
from sqlalchemy.orm import declarative_base, relationship



# DSN = "postgresql://postgres:happy1228@localhost:5432/netology_db"
# engine = sq.create_engine(DSN)

# conn = engine.connect()

Base = declarative_base()

class Publisher(Base):
    __tablename__ = "publisher"

    id = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String(length=120), unique=True)

class Book(Base):
    __tablename__ = "book"

    id = sq.Column(sq.Integer, primary_key=True)
    title = sq.Column(sq.String, unique=True)
    id_publisher = sq.Column(sq.Integer, sq.ForeignKey("publisher.id"))
   
    publisher = relationship(Publisher, backref="book")
    
class Shop(Base):
    __tablename__ = "shop"

    id = sq.Column(sq.Integer, primary_key=True)
    name = sq.Column(sq.String(length=120), unique=True)
    
    def __str__ (self):
        return f'Course {self.id}: {self.name}'
    
class Stock(Base):
    __tablename__ = "stock"

    id = sq.Column(sq.Integer, primary_key=True)
    id_book = sq.Column(sq.Integer, sq.ForeignKey("book.id"), nullable=False)
    id_shop = sq.Column(sq.Integer, sq.ForeignKey("shop.id"), nullable=False)
    count = sq.Column(sq.Integer)
    
    book = relationship(Book, backref="stock")
    shop = relationship(Shop, backref="stock")
    
    def __str__ (self):
        return f'Course {self.id}: {self.count}, {self.id_book}, {self.id_shop}'
    
class Sale(Base):
    __tablename__ = "sale"

    id = sq.Column(sq.Integer, primary_key=True)
    price = sq.Column(sq.Float)
    date_sale = sq.Column(sq.Date)
    id_stock = sq.Column(sq.Integer, sq.ForeignKey("stock.id"), nullable=False)
    count = sq.Column(sq.Integer)
    
    stock = relationship(Stock, backref="id_stock")
    
    def __str__ (self):
        return f'Course {self.id}: {self.price}, {self.date_sale}, {self.id_stock}, {self.count}'


def create_tables(engine):
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)


# create_tables(engine)



