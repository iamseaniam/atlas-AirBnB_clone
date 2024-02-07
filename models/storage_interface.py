# models/storage_interface.py
import uuid
from datetime import datetime

class StorageInterface:
    _storage = None

    def __init__(self, *args, **kwargs):
        from models.engine.file_storage import FileStorage  # Move the import here
        self._storage = kwargs.pop('storage', None)
        if args:
            for arg in args:
                if isinstance(arg, FileStorage):
                    self._storage = arg
                    break
        super().__init__(*args, **kwargs)

    def save(self):
        """updates attribute updated_at with current datetime"""
        self.updated_at = datetime.now()
        if hasattr(self, '_storage'):
            self._storage.save(self)

    def to_dict(self):
        """DICTIONARY"""
        obj_dict = self.__dict__.copy()
        obj_dict["__class__"] = self.__class__.__name__
        obj_dict["created_at"] = obj_dict["created_at"].isoformat()
        obj_dict["updated_at"] = obj_dict["updated_at"].isoformat()
        return obj_dict
