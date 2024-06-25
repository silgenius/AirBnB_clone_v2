#!/usr/bin/python3

"""
Module that prints the State object with the name passed as argument from the
database hbtn_0e_6_usa
"""

if __name__ == "__main__":

    from models.state import State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from os import getenv

    username = "hbnb_dev"
    password = "hbnb_dev_pwd"
    database = "hbnb_dev_db"

    engine = create_engine(f'mysql+mysqldb://{username}:{password}@localhost/{database}', pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State.id, State.name)

    if states:
        for state in states:
            print(f'{state[0]}, {state[1]}')
    else:
        print("Not found")

    session.close()
