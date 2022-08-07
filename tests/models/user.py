#!/usr/bin/python3
"""user module: contains User class"""


from models.base_model import BaseModel


class User(BaseModel):
    """defines individual users"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
