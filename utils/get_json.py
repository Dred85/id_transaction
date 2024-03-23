import json


def get_json():
    """
    Получем дынные из json файла
    """
    with open('C:\\Users\\DRED\\PycharmProject\\id_transactions\\data\\operations.json', 'r', encoding="utf-8") as file:
        return json.load(file)





