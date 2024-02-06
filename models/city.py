#!/usr/bin/python3
"We built this class! We built this class on rock and roll!"

from models.base_model import BaseModel


class City(BaseModel):
    "city class"
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
