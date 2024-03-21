import os
import json


def get_json():
    """
    Получем дынные из json файла
    """
    with open(os.path.join("id_transactions", "data", "operations.json")) as file:
        return json.load(file)


print(get_json())
