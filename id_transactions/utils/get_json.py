import os
import json


def get_json():
    """
    Получем дынные из json файла
    """
    with open('operations.json', 'r', encoding="utf-8") as file:
        return json.load(file)


# print(get_json())
