#!/usr/bin/python3
"""
This class handles the serialization and deserialization of
BaseModel instances to and from a JSON file.
"""
import json
from models.base_model import BaseModel


class FileStorage:
    """
    Serializes and deserializes objects to a JSON file.

    Attributes:
        __file_path (str): The path to the JSON file.
        __objects (dict): A dictionary storing all objects by
                          <class name>.id (ex: BaseModel.1212)
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns the dictionary __objects.
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        Sets in __objects the obj with key <obj class name>.id.

        Args:
            obj (BaseModel): The object to add.        
        """
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """
        Serializes __objects to a JSON file at __file_path.
        """
        obj_dict = {}
        for key, value in FileStorage.__objects.items():
            obj_dict[key] = FileStorage.__objects[key].to_dict()
        with open(FileStorage.__file_path, "w", encoding="utf-8") as file:
            json.dump(obj_dict, file)

    def reload(self):
        """
        Deserializes the JSON file at __file_path
        to __objects (if it exists).
        """
        try:
            with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
                for key, value in (json.load(f)).items():
                    value = eval(value["__class__"])(**value)
                    self.__objects[key] = value
        except Exception:
            pass        
