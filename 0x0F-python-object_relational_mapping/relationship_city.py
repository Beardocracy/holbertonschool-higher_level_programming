#!/usr/bin/python3
''' Contains the class definition of a city for sqlalchemy '''


from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from relationship_state import State, Base


class City(Base):
    ''' Definition of city class '''
    __tablename__ = "cities"
    id = Column(Integer, nullable=False, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
