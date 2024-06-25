#!/usr/bin/python3

"""
Module that prints the State object with the name passed as argument from the
database hbtn_0e_6_usa
"""

if __name__ == "__main__":

    from models.state import State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    import sys

    username = "hbnb_test"
    password = "hbnb_test_pwd"
    database = "hbnb_test_db"

    engine = create_engine(f'mysql+mysqldb://{username}:{password}@localhost/{database}', pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State.id, State.name).first()

    if state:
        print(f'{state[0]}, {state[1]}')
    else:
        print("Not found")

    session.close()
