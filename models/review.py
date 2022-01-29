#!/usr/bin/python3
"""
import modules
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """class for reviews"""
    place_id = ""
    user_id = ""
    text = ""
