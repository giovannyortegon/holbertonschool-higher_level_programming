#!/usr/bin/python3
""" Start link class to table in database """
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def main():
    """ Connect and Read Data Base """
    db = 'mysql+mysqldb://{}:{}@localhost/{}'.format(
          sys.argv[1], sys.argv[2], sys.argv[3], pool_pre_ping=True)
    # Create connection
    engine = create_engine(db)
    # Open session
    Session = sessionmaker(bind=engine)
    session = Session()
    # Adding
    state = State(name='Louisiana')
    session.add(state)
    session.commit()
    # Query
    _name = 'Louisiana'
    records = session.query(State).filter(State.name == _name)

    for record in records:
        print('{}'.format(record.id))
    # Close connection
    session.close()


if __name__ == "__main__":
    main()
