#!/usr/bin/python3
"is this sort of airbnb thing i am too broke to understand?"

from models.base_model import BaseModel


class Amenity(BaseModel):
    "this class does rich people things"
    name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
