#!/usr/bin/python3

from models.base_model import BaseModel
from models.state import State

state = State(name='California')

print(state.name)
print(state.id)
