#!/usr/bin/python3 
from .base_model import BaseModel
from .city import City
from .amenity import Amenity
from .place import Place
from .review import Review
from .state import State
from .user import User

classes = {
    'BaseModel': BaseModel,
    'City': City,
    'Amenity': Amenity,
    'Place': Place,
    'Review': Review,
    'State': State,
    'User': User
}