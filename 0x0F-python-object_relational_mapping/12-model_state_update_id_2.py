#!/usr/bin/python3
''' Adds Louisiana to the DB '''


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

    state = session.query(State).filter(State.id == 2).one_or_none()
    if state is not None:
        state.name = "New Mexico"
        session.commit()
    session.close()
