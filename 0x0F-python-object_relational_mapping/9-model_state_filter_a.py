#!/usr/bin/python3
''' Lists all states with an a in the name '''


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
    states = session.query(State).order_by(State.id).all()
    for row in states:
        if 'a' in row.name:
            print("{}: {}".format(row.id, row.name))
    session.close()
