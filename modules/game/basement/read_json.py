'''
Цей модуль читає `json`
'''
import os
import json

def read_json(fd: str) -> dict:
    '''
    Читає `json` у вказаному файлу та повертає це у `dict`
    '''
    path_to_file = os.path.abspath(__file__ + f"/../../static/{fd}")
    with open(path_to_file, "r") as file:
        return json.load(file)