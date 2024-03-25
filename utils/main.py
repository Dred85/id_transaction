import os

from config import ROOT_DIR
from utils.sorted_json import sorted_json
from utils.get_json import get_json
from utils.format_operation import format_operation


def main():
    """" Окончательный Вывод 5 ближайших к нашай дате транзакции """

    # В цикле, при помощи среза sorted_json(get_json())[:5], выводим 5 ближайших к нашай дате транзакции,
    # разделенных пробелами
    for operation in sorted_json(get_json(path_to_file))[:5]:
        print(format_operation(operation['date'], operation['description'], operation.get('from', ''),
                               operation.get('to', ''), operation['operationAmount']['amount'],
                               operation['operationAmount']['currency']))
        print()


# Путь до файла operations.json через абсолютный путь ROOT_DIR
path_to_file = os.path.join(ROOT_DIR, 'data', 'operations.json')

main()
