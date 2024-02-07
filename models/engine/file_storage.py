#!/usr/bin/python3
"""Defines the FileStorage class."""
import json

class FileStorage:
    """Represents a storage engine.

    Attributes:
        _file_path (str): The file where the objects are saved
        _objects (dict):A dictionary of instantiated objects.
    """
    __file_path = "file.json"
    __objects = {}
def to_dict(self):
        """Return a dictionary representation of the BaseModel instance."""
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()

    def all(self):
        """Return the dictionary __objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Set in _objects obj with key <obj_class_name>.id"""
        class_name = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(class_name, obj.id)] = obj

    def save(self):
        """Serialize __objects to the JSON file"""
        stored_dict = FileStorage.__objects
        obj_dict = {obj : stored_dict[obj].to_dict() for obj in 
                stored_dict.keys()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(obj_dict, f)

    def reload(self):
        """Deserialize the JSON file __file_path to __objects,if it exists.:"""
        try:
            with open(FileStorage.__file_path) as f:
                obj_dict = json.load(f)
                for key, value in obj_dict.items():
                    class_name, object_id = key.split('.')
                    class_ = eval(class_name)
                    self.__objects[key] = class_(**value)
        except FileNotFoundError:
            pass



