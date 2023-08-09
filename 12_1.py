from sqlalchemy import INT, String, Column, DateTime, ForeignKey, VARCHAR, TEXT, TIMESTAMP
from sqlalchemy.orm import DeclarativeBase, relationship
from datetime import datetime

class Base(DeclarativeBase):
    pass

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
    date_of_birth = Column(INT, nullable=False)
    date_created = Column(TIMESTAMP, default=datetime.utcnow())
    date_updated = Column(TIMESTAMP, onupdate=datetime.utcnow())
    date_id = Column(VARCHAR(64), ForeignKey('dates.id', onupdate='CASCADE'), nullable=False)
    date = relationship(Dates, back_populates='dates')