import json


def get_json(path_to_file):
    """
    Получаем несортированные дынные из json файла
    """

    with open(path_to_file, 'r', encoding="utf-8") as file:
        return json.load(file)
