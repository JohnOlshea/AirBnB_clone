#!/usr/bin/python3
"""Importing Base Model"""
from models.base_model import BaseModel


class City(BaseModel):
    """City class that inherits from BaseModel"""

    name = ""
    state_id = ""
