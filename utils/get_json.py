import os
import json


def get_json():
    """
    Получаем несортированные дынные из json файла
    """
    file_ = os.path.join('..', 'data', 'operations.json')
    with open(file_, 'r', encoding="utf-8") as file:
        return json.load(file)
