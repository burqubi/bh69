from sqlalchemy import INT, String, Column, DateTime, ForeignKey, VARCHAR, TEXT, TIMESTAMP
from sqlalchemy.orm import DeclarativeBase, relationship, sessionmaker
from datetime import datetime

class Base(DeclarativeBase):
    session = sessionmaker(bind=engine)

class Dates(Base):
    __tablename__ = 'dates'
    id = Column(INT, primary_key=True)
    date = Column(VARCHAR(10), nullable=False)
    events = Column(VARCHAR(64), nullable=False)
    description = Column(TEXT, nullable=False)
    date_created = Column(TIMESTAMP, default=datetime.utcnow())
    date_updated = Column(TIMESTAMP, onupdate=datetime.utcnow())
    birth = relationship('Birthdays', back_populates='birthdays')

class Birthdays(Base):
    __tablename__ = 'birthdays'
    id = Column(INT, primary_key=True)
    cel_name = Column(VARCHAR(64), nullable=False)
    date_of_birth = Column(VARCHAR(10), nullable=False)
    date_created = Column(TIMESTAMP, default=datetime.utcnow())
    date_updated = Column(TIMESTAMP, onupdate=datetime.utcnow())
    date_id = Column(VARCHAR(64), ForeignKey('dates.id', onupdate='CASCADE'), nullable=False)
    date = relationship(Dates, back_populates='dates')




class Base(DeclarativeBase):
    engine = create_engine(url='')
    session = sessionmaker(bind=engine)

from pydantic import BaseModel

def load_names_to_db(objs: list):
    objs = [Dates(**obj.date()) for obj in objs]
    with Date.session as session:
        session.add_all(objs)
        try:
            session.commit()
        except:
            pass

# def class_new() -> list[Dates]:
#     with Dates.session as session:
#         objs = session.scalars(select(Dates))
#         return [Birthdays]