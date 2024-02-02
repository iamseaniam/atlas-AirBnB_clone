#!/usr/bin/python3
"""BaseModel"""

import uuid
import datetime

class BaseModel():
    """better documentation coming soon"""
    __nb_objects = 0
    
    def __init__(self, id=None):
        """Checks for id. If it doesn't have id, a new one is created along with the current time."""
        if id is not None:
            self.id = id
        else:
            new_uuid = uuid.uuid4()
            self.id = str(new_uuid)
            
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()
        
    def update(self):
        self.updated_at = datetime.datetime.now()