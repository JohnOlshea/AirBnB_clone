#!/usr/bin/python3

"""BaseModel class for all other models in the project.

This class provides common attributes and methods for other models to inherit from.
"""

import uuid
from datetime import datetime

class BaseModel:
    """
    BaseModel class represents the base model for other classes.
    It defines common attributes and methods for other classes.
    """

    def __init__(self):
        """
        Initializes a new instance of BaseModel.

        Attributes:
            id (str): Unique identifier for the instance.
            created_at (datetime): Date and time when the instance is created.
            updated_at (datetime): Date and time when the instance is last updated.
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def __str__(self):
        """
        Returns a string representation of the BaseModel instance.
        """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """
        Updates the 'updated_at' attribute with the current date and time.
        """        
        self.updated_at = datetime.now()

    def to_dict(self):
        """
        Returns a dictionary representation of the object with ISO formatted timestamps.

        This dictionary can be used for serialization purposes.
        """        
        model_dict = self.__dict__.copy()
        model_dict["__class__"] = self.__class__.__name__
        model_dict["created_at"] = model_dict["created_at"].isoformat()
        model_dict["updated_at"] = model_dict["updated_at"].isoformat()
        return model_dict
