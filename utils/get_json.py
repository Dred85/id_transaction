import os
import json


def get_json():
    """
    Получаем несортированные дынные из json файла
    """

    # Абсолютный путь до папки utils
    current_dir = os.path.dirname(__file__)

    file_ = os.path.join(current_dir, '..', 'data', 'operations.json')

    with open(file_, 'r', encoding="utf-8") as file:
        return json.load(file)
