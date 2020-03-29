#!/usr/bin/python3
''' Contains the class definition of a state '''


from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy import relationship


Base = declarative_base()


class State(Base):
    ''' Definition of state class '''
    __tablename__ = "states"
    id = Column(Integer, nullable=False, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state",
                          cascade="all, delete-orphan")
