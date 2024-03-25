import os
import json

from config import ROOT_DIR


def get_json():
    """
    Получаем несортированные дынные из json файла
    """

    # Абсолютный путь до папки utils через ROOT_DIR
    file_ = os.path.join(ROOT_DIR, 'data', 'operations.json')

    with open(file_, 'r', encoding="utf-8") as file:
        return json.load(file)
