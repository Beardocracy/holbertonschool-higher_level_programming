#!/usr/bin/python3
''' Deletes states with an a '''


if __name__ == "__main__":
    import sys
    from model_state import Base, State
    from sqlalchemy import (create_engine, Table, Integer, String, Column)
    from sqlalchemy.orm import sessionmaker

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    Base.metadata.create_all(engine)
    Session = sessionmaker()
    Session.configure(bind=engine)
    session = Session()

    session.query(State).filter(State.name.like('%a%'))\
           .delete(synchronize_session='fetch')
    session.commit()
    session.close()
