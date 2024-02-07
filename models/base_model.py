#!/usr/bin/python3
"""
     Project  0x00. AirBnB clone - The console
     The BaseModel class
         Methods:
             __str__: returns a string rep of instance
             save: updates attributes
             to_dict: returns dict of key values
"""
# models/base_model.py
from datetime import datetime
import uuid

class BaseModel:
    def __init__(self, *args, **kwargs):
        self.id = kwargs.get('id', str(uuid.uuid4()))
        self.created_at = kwargs.get('created_at', datetime.now())
        self.updated_at = kwargs.get('updated_at', self.created_at)

    def save(self):
        """Save the instance to the storage"""
        from models.engine.file_storage import FileStorage
        storage = FileStorage()
        storage.save(self)

    def to_dict(self):
        """Returns a dictionary containing the object's attributes"""
        return {
            'id': self.id,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat(),
            '__class__': self.__class__.__name__
        }
